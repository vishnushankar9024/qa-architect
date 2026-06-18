import {
  Alert,
  Button,
  Card,
  CardContent,
  Chip,
  MenuItem,
  Stack,
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableRow,
  TextField,
  Typography
} from "@mui/material";
import { useState } from "react";

import type { KnowledgeSource, Project } from "../types";
import { ProjectSelector } from "../components/ProjectSelector";

interface KnowledgeSourcesPageProps {
  projects: Project[];
  selectedProjectId: string;
  sources: KnowledgeSource[];
  onSelectProject: (projectId: string) => void;
  onAddRepositorySource: (payload: {
    sourceType: string;
    url: string;
    createdBy: string;
  }) => Promise<void>;
  onUploadDocumentSources: (files: File[]) => Promise<void>;
}

const repositoryTypes = ["GitHub URL", "GitLab URL", "Bitbucket URL"];

export function KnowledgeSourcesPage({
  projects,
  selectedProjectId,
  sources,
  onSelectProject,
  onAddRepositorySource,
  onUploadDocumentSources
}: KnowledgeSourcesPageProps) {
  const [repoType, setRepoType] = useState(repositoryTypes[0]);
  const [repoUrl, setRepoUrl] = useState("");
  const [selectedFiles, setSelectedFiles] = useState<File[]>([]);

  return (
    <Stack spacing={3}>
      <Typography variant="h4">Knowledge Sources</Typography>
      <ProjectSelector
        projects={projects}
        selectedProjectId={selectedProjectId}
        onSelect={onSelectProject}
      />
      {!selectedProjectId ? (
        <Alert severity="info">Select a project before registering sources.</Alert>
      ) : null}
      <Stack direction={{ xs: "column", lg: "row" }} spacing={2}>
        <Card sx={{ flex: 1 }}>
          <CardContent>
            <Stack spacing={2}>
              <Typography variant="h6">Repository Source</Typography>
              <TextField
                select
                label="Repository Type"
                value={repoType}
                onChange={(event) => setRepoType(event.target.value)}
              >
                {repositoryTypes.map((type) => (
                  <MenuItem key={type} value={type}>
                    {type}
                  </MenuItem>
                ))}
              </TextField>
              <TextField
                label="Repository URL"
                placeholder="https://github.com/org/repo"
                value={repoUrl}
                onChange={(event) => setRepoUrl(event.target.value)}
              />
              <Button
                variant="contained"
                disabled={!selectedProjectId || !repoUrl}
                onClick={async () => {
                  await onAddRepositorySource({
                    sourceType: repoType,
                    url: repoUrl,
                    createdBy: "qa.architect"
                  });
                  setRepoUrl("");
                }}
              >
                Connect Repository
              </Button>
            </Stack>
          </CardContent>
        </Card>
        <Card sx={{ flex: 1 }}>
          <CardContent>
            <Stack spacing={2}>
              <Typography variant="h6">Document Sources (multi-file, metadata only)</Typography>
              <Alert severity="info">
                Supported: PDF, DOCX, XLSX, PPTX, TXT, Markdown. Multiple files can be uploaded
                together.
              </Alert>
              <Button component="label" variant="outlined" disabled={!selectedProjectId}>
                Select Documents
                <input
                  hidden
                  multiple
                  type="file"
                  accept=".pdf,.docx,.xlsx,.pptx,.txt,.md,.markdown"
                  onChange={(event) => {
                    const files = Array.from(event.target.files ?? []);
                    setSelectedFiles(files);
                    event.target.value = "";
                  }}
                />
              </Button>
              {selectedFiles.length > 0 ? (
                <Stack direction="row" spacing={1} useFlexGap flexWrap="wrap">
                  {selectedFiles.map((file) => (
                    <Chip key={`${file.name}-${file.lastModified}`} label={file.name} />
                  ))}
                </Stack>
              ) : null}
              <Button
                variant="contained"
                disabled={!selectedProjectId || selectedFiles.length === 0}
                onClick={async () => {
                  await onUploadDocumentSources(selectedFiles);
                  setSelectedFiles([]);
                }}
              >
                Register Documents
              </Button>
            </Stack>
          </CardContent>
        </Card>
      </Stack>
      <Card>
        <CardContent>
          <Typography variant="h6" gutterBottom>
            Source Registration Framework
          </Typography>
          <Table size="small">
            <TableHead>
              <TableRow>
                <TableCell>Type</TableCell>
                <TableCell>Status</TableCell>
                <TableCell>Metadata</TableCell>
                <TableCell>Created</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {sources.map((source) => (
                <TableRow key={source.id}>
                  <TableCell>{source.sourceType}</TableCell>
                  <TableCell>{source.status}</TableCell>
                  <TableCell>{JSON.stringify(source.metadata)}</TableCell>
                  <TableCell>{new Date(source.createdDate).toLocaleString()}</TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </CardContent>
      </Card>
    </Stack>
  );
}
