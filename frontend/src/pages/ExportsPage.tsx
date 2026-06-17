import DownloadIcon from "@mui/icons-material/Download";
import { Alert, Button, Card, CardContent, Stack, TextField, Typography } from "@mui/material";
import { useState } from "react";

import { ProjectSelector } from "../components/ProjectSelector";
import type { Project } from "../types";

interface ExportsPageProps {
  projects: Project[];
  selectedProjectId: string;
  onSelectProject: (projectId: string) => void;
  onExport: (format: "json" | "markdown" | "csv") => Promise<string>;
}

export function ExportsPage({
  projects,
  selectedProjectId,
  onSelectProject,
  onExport
}: ExportsPageProps) {
  const [content, setContent] = useState("");

  return (
    <Stack spacing={3}>
      <Typography variant="h4">Exports</Typography>
      <ProjectSelector
        projects={projects}
        selectedProjectId={selectedProjectId}
        onSelect={onSelectProject}
      />
      {!selectedProjectId ? (
        <Alert severity="info">Select a project to export the approved knowledge pack.</Alert>
      ) : null}
      <Stack direction="row" spacing={2}>
        <Button
          variant="contained"
          startIcon={<DownloadIcon />}
          disabled={!selectedProjectId}
          onClick={async () => setContent(await onExport("json"))}
        >
          Export JSON
        </Button>
        <Button
          variant="contained"
          startIcon={<DownloadIcon />}
          disabled={!selectedProjectId}
          onClick={async () => setContent(await onExport("markdown"))}
        >
          Export Markdown
        </Button>
        <Button
          variant="contained"
          startIcon={<DownloadIcon />}
          disabled={!selectedProjectId}
          onClick={async () => setContent(await onExport("csv"))}
        >
          Export CSV
        </Button>
      </Stack>
      <Card>
        <CardContent>
          <Typography variant="h6" gutterBottom>
            Knowledge Pack Preview
          </Typography>
          <TextField
            fullWidth
            multiline
            minRows={16}
            value={content}
            placeholder="Generated export preview appears here."
            InputProps={{ readOnly: true }}
          />
        </CardContent>
      </Card>
    </Stack>
  );
}
