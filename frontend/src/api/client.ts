import type {
  DashboardMetrics,
  KnowledgeBase,
  KnowledgeSource,
  Project
} from "../types";

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL ?? "http://127.0.0.1:8000";

async function request<T>(path: string, options?: RequestInit): Promise<T> {
  const response = await fetch(`${API_BASE_URL}${path}`, {
    headers: {
      "Content-Type": "application/json",
      ...(options?.headers ?? {})
    },
    ...options
  });

  if (!response.ok) {
    const text = await response.text();
    throw new Error(text || `Request failed: ${response.status}`);
  }

  const contentType = response.headers.get("content-type") ?? "";
  if (contentType.includes("application/json")) {
    return (await response.json()) as T;
  }
  return (await response.text()) as T;
}

export const api = {
  listProjects: () => request<Project[]>("/projects"),
  createProject: (payload: {
    name: string;
    description: string;
    createdBy: string;
  }) =>
    request<Project>("/projects", {
      method: "POST",
      body: JSON.stringify(payload)
    }),
  getProject: (projectId: string) => request<Project>(`/project/${projectId}`),
  addRepositorySource: (
    projectId: string,
    payload: { sourceType: string; url: string; createdBy: string }
  ) =>
    request<KnowledgeSource>(`/projects/${projectId}/sources/repository`, {
      method: "POST",
      body: JSON.stringify(payload)
    }),
  addDocumentSource: (
    projectId: string,
    payload: {
      sourceType: string;
      fileName: string;
      fileSizeBytes: number;
      createdBy: string;
    }
  ) =>
    request<KnowledgeSource>(`/projects/${projectId}/sources/document`, {
      method: "POST",
      body: JSON.stringify(payload)
    }),
  listSources: (projectId: string) =>
    request<KnowledgeSource[]>(`/projects/${projectId}/sources`),
  generateKnowledgeBase: (projectId: string) =>
    request<KnowledgeBase>(`/knowledge-base/${projectId}`, { method: "POST" }),
  getKnowledgeBase: (projectId: string) =>
    request<KnowledgeBase>(`/knowledge-base/${projectId}`),
  reviewItem: (payload: {
    projectId: string;
    artifactType: string;
    itemId: string;
    action: "approve" | "reject" | "edit";
    reviewer: string;
    name?: string;
    description?: string;
  }) =>
    request("/review", {
      method: "POST",
      body: JSON.stringify(payload)
    }),
  getDashboardMetrics: (projectId: string) =>
    request<DashboardMetrics>(`/knowledge-base/${projectId}/dashboard`),
  exportKnowledge: (projectId: string, format: "json" | "markdown" | "csv") =>
    request<string>(`/export/${projectId}?format=${format}`)
};
