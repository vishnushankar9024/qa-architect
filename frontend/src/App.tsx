import { Alert, Snackbar } from "@mui/material";
import { useEffect, useMemo, useState } from "react";
import { Navigate, Route, Routes } from "react-router-dom";

import { api } from "./api/client";
import { AppLayout } from "./layout/AppLayout";
import { ExportsPage } from "./pages/ExportsPage";
import { KnowledgeDashboardPage } from "./pages/KnowledgeDashboardPage";
import { KnowledgeSourcesPage } from "./pages/KnowledgeSourcesPage";
import { ProjectsPage } from "./pages/ProjectsPage";
import { ReviewPage } from "./pages/ReviewPage";
import type { DashboardMetrics, KnowledgeBase, KnowledgeSource, Project, ReviewableItem } from "./types";

export default function App() {
  const [projects, setProjects] = useState<Project[]>([]);
  const [selectedProjectId, setSelectedProjectId] = useState("");
  const [sources, setSources] = useState<KnowledgeSource[]>([]);
  const [knowledgeBase, setKnowledgeBase] = useState<KnowledgeBase | null>(null);
  const [metrics, setMetrics] = useState<DashboardMetrics | null>(null);
  const [successMessage, setSuccessMessage] = useState<string | null>(null);
  const [errorMessage, setErrorMessage] = useState<string | null>(null);

  async function loadProjects(): Promise<void> {
    try {
      const data = await api.listProjects();
      setProjects(data);
      if (!selectedProjectId && data.length > 0) {
        setSelectedProjectId(data[0].id);
      }
    } catch (error) {
      setErrorMessage((error as Error).message);
    }
  }

  async function loadProjectData(projectId: string): Promise<void> {
    if (!projectId) {
      setSources([]);
      setKnowledgeBase(null);
      setMetrics(null);
      return;
    }
    try {
      const sourceData = await api.listSources(projectId);
      setSources(sourceData);
    } catch {
      setSources([]);
    }

    try {
      const kb = await api.getKnowledgeBase(projectId);
      setKnowledgeBase(kb);
    } catch {
      setKnowledgeBase(null);
    }
    try {
      const dashboard = await api.getDashboardMetrics(projectId);
      setMetrics(dashboard);
    } catch {
      setMetrics(null);
    }
  }

  useEffect(() => {
    void loadProjects();
  }, []);

  useEffect(() => {
    void loadProjectData(selectedProjectId);
  }, [selectedProjectId]);

  const handleReview =
    (artifactType: "features" | "domains" | "business_rules" | "flows") =>
    async (
      item: ReviewableItem,
      action: "approve" | "reject" | "edit",
      payload?: { name?: string; description?: string }
    ) => {
      if (!selectedProjectId) {
        return;
      }
      try {
        await api.reviewItem({
          projectId: selectedProjectId,
          artifactType,
          itemId: item.id,
          action,
          reviewer: "lead.reviewer",
          ...payload
        });
        setSuccessMessage(`${artifactType} updated (${action}).`);
        await loadProjects();
        await loadProjectData(selectedProjectId);
      } catch (error) {
        setErrorMessage((error as Error).message);
      }
    };

  const featureItems = useMemo(() => knowledgeBase?.features ?? [], [knowledgeBase]);
  const domainItems = useMemo(() => knowledgeBase?.domains ?? [], [knowledgeBase]);
  const ruleItems = useMemo(() => knowledgeBase?.business_rules ?? [], [knowledgeBase]);
  const flowItems = useMemo(() => knowledgeBase?.flows ?? [], [knowledgeBase]);

  return (
    <AppLayout>
      <Routes>
        <Route
          path="/"
          element={
            <ProjectsPage
              projects={projects}
              selectedProjectId={selectedProjectId}
              onSelectProject={setSelectedProjectId}
              feedback={successMessage}
              onCreateProject={async (payload) => {
                await api.createProject(payload);
                await loadProjects();
                setSuccessMessage("Project created.");
              }}
              onGenerateKnowledgeBase={async () => {
                if (!selectedProjectId) {
                  return;
                }
                await api.generateKnowledgeBase(selectedProjectId);
                await loadProjects();
                await loadProjectData(selectedProjectId);
                setSuccessMessage("Knowledge base generated using QA Architect stages.");
              }}
            />
          }
        />
        <Route
          path="/sources"
          element={
            <KnowledgeSourcesPage
              projects={projects}
              selectedProjectId={selectedProjectId}
              sources={sources}
              onSelectProject={setSelectedProjectId}
              onAddRepositorySource={async (payload) => {
                if (!selectedProjectId) {
                  return;
                }
                await api.addRepositorySource(selectedProjectId, payload);
                await loadProjectData(selectedProjectId);
                setSuccessMessage("Repository source registered.");
              }}
              onUploadDocumentSources={async (files) => {
                if (!selectedProjectId) {
                  return;
                }
                await api.uploadDocumentSources(selectedProjectId, {
                  createdBy: "qa.architect",
                  files
                });
                await loadProjectData(selectedProjectId);
                setSuccessMessage(`Document metadata registered for ${files.length} file(s).`);
              }}
            />
          }
        />
        <Route
          path="/dashboard"
          element={
            <KnowledgeDashboardPage
              projects={projects}
              selectedProjectId={selectedProjectId}
              onSelectProject={setSelectedProjectId}
              metrics={metrics}
            />
          }
        />
        <Route
          path="/features"
          element={
            <ReviewPage
              title="Features Review"
              projects={projects}
              selectedProjectId={selectedProjectId}
              onSelectProject={setSelectedProjectId}
              items={featureItems}
              onReview={handleReview("features")}
            />
          }
        />
        <Route
          path="/domains"
          element={
            <ReviewPage
              title="Domains Review"
              projects={projects}
              selectedProjectId={selectedProjectId}
              onSelectProject={setSelectedProjectId}
              items={domainItems}
              onReview={handleReview("domains")}
            />
          }
        />
        <Route
          path="/business-rules"
          element={
            <ReviewPage
              title="Business Rules Review"
              projects={projects}
              selectedProjectId={selectedProjectId}
              onSelectProject={setSelectedProjectId}
              items={ruleItems}
              onReview={handleReview("business_rules")}
            />
          }
        />
        <Route
          path="/flows"
          element={
            <ReviewPage
              title="Flow Review"
              projects={projects}
              selectedProjectId={selectedProjectId}
              onSelectProject={setSelectedProjectId}
              items={flowItems}
              onReview={handleReview("flows")}
            />
          }
        />
        <Route
          path="/exports"
          element={
            <ExportsPage
              projects={projects}
              selectedProjectId={selectedProjectId}
              onSelectProject={setSelectedProjectId}
              onExport={async (format) => {
                if (!selectedProjectId) {
                  return "";
                }
                const data = await api.exportKnowledge(selectedProjectId, format);
                setSuccessMessage(`Knowledge Pack exported as ${format.toUpperCase()}.`);
                return data;
              }}
            />
          }
        />
        <Route path="*" element={<Navigate to="/" />} />
      </Routes>
      <Snackbar
        open={Boolean(successMessage)}
        autoHideDuration={4000}
        onClose={() => setSuccessMessage(null)}
      >
        <Alert severity="success" onClose={() => setSuccessMessage(null)}>
          {successMessage}
        </Alert>
      </Snackbar>
      <Snackbar open={Boolean(errorMessage)} autoHideDuration={5000} onClose={() => setErrorMessage(null)}>
        <Alert severity="error" onClose={() => setErrorMessage(null)}>
          {errorMessage}
        </Alert>
      </Snackbar>
    </AppLayout>
  );
}
