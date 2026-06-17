import AutoFixHighIcon from "@mui/icons-material/AutoFixHigh";
import {
  Alert,
  Button,
  Card,
  CardContent,
  Chip,
  Grid,
  Paper,
  Stack,
  TextField,
  Typography
} from "@mui/material";
import { useState } from "react";

import { ProjectSelector } from "../components/ProjectSelector";
import type { Project } from "../types";

interface ProjectsPageProps {
  projects: Project[];
  selectedProjectId: string;
  onSelectProject: (projectId: string) => void;
  onCreateProject: (payload: {
    name: string;
    description: string;
    createdBy: string;
  }) => Promise<void>;
  onGenerateKnowledgeBase: () => Promise<void>;
  feedback: string | null;
}

export function ProjectsPage({
  projects,
  selectedProjectId,
  onSelectProject,
  onCreateProject,
  onGenerateKnowledgeBase,
  feedback
}: ProjectsPageProps): JSX.Element {
  const [name, setName] = useState("");
  const [description, setDescription] = useState("");
  const [createdBy, setCreatedBy] = useState("qa.architect");

  const selectedProject = projects.find((project) => project.id === selectedProjectId);

  return (
    <Stack spacing={3}>
      <Typography variant="h4">Projects</Typography>
      {feedback ? <Alert severity="success">{feedback}</Alert> : null}
      <Grid container spacing={3}>
        <Grid size={{ xs: 12, md: 4 }}>
          <Card>
            <CardContent>
              <Stack spacing={2}>
                <Typography variant="h6">Create Project</Typography>
                <TextField
                  label="Project Name"
                  value={name}
                  onChange={(event) => setName(event.target.value)}
                />
                <TextField
                  label="Description"
                  multiline
                  minRows={3}
                  value={description}
                  onChange={(event) => setDescription(event.target.value)}
                />
                <TextField
                  label="Created By"
                  value={createdBy}
                  onChange={(event) => setCreatedBy(event.target.value)}
                />
                <Button
                  variant="contained"
                  onClick={async () => {
                    await onCreateProject({ name, description, createdBy });
                    setName("");
                    setDescription("");
                  }}
                  disabled={!name || !createdBy}
                >
                  Create Project
                </Button>
              </Stack>
            </CardContent>
          </Card>
        </Grid>
        <Grid size={{ xs: 12, md: 8 }}>
          <Stack spacing={2}>
            <ProjectSelector
              projects={projects}
              selectedProjectId={selectedProjectId}
              onSelect={onSelectProject}
            />
            {selectedProject ? (
              <Paper sx={{ p: 2 }}>
                <Stack spacing={2}>
                  <Typography variant="h6">Project Dashboard</Typography>
                  <Typography variant="body1">{selectedProject.description}</Typography>
                  <Stack direction="row" spacing={1}>
                    <Chip label={`Status: ${selectedProject.status}`} />
                    <Chip label={`Created by: ${selectedProject.createdBy}`} />
                  </Stack>
                  <Button
                    variant="contained"
                    startIcon={<AutoFixHighIcon />}
                    onClick={onGenerateKnowledgeBase}
                  >
                    Generate Knowledge Base
                  </Button>
                </Stack>
              </Paper>
            ) : (
              <Alert severity="info">Create and select a project to begin.</Alert>
            )}
          </Stack>
        </Grid>
      </Grid>
    </Stack>
  );
}
