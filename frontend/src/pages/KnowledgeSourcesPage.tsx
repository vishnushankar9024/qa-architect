import {
  Alert,
  Button,
  Card,
  CardContent,
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
  onAddDocumentSource: (payload: {
    sourceType: string;
    fileName: string;
    fileSizeBytes: number;
    createdBy: string;
  }) => Promise<void>;
}

const repositoryTypes = ["GitHub URL", "GitLab URL", "Bitbucket URL"];
const documentTypes = ["PDF", "DOCX", "XLSX", "PPTX", "TXT", "Markdown"];

export function KnowledgeSourcesPage({
  projects,
  selectedProjectId,
  sources,
  onSelectProject,
  onAddRepositorySource,
  onAddDocumentSource
}: KnowledgeSourcesPageProps) {
  const [repoType, setRepoType] = useState(repositoryTypes[0]);
  const [repoUrl, setRepoUrl] = useState("");
  const [documentType, setDocumentType] = useState(documentTypes[0]);
  const [fileName, setFileName] = useState("");
  const [fileSizeBytes, setFileSizeBytes] = useState("0");

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
              <Typography variant="h6">Document Source (metadata only)</Typography>
              <TextField
                select
                label="Document Type"
                value={documentType}
                onChange={(event) => setDocumentType(event.target.value)}
              >
                {documentTypes.map((type) => (
                  <MenuItem key={type} value={type}>
                    {type}
                  </MenuItem>
                ))}
              </TextField>
              <TextField
                label="File Name"
                placeholder="requirements.md"
                value={fileName}
                onChange={(event) => setFileName(event.target.value)}
              />
              <TextField
                label="File Size (bytes)"
                value={fileSizeBytes}
                onChange={(event) => setFileSizeBytes(event.target.value)}
              />
              <Button
                variant="contained"
                disabled={!selectedProjectId || !fileName}
                onClick={async () => {
                  await onAddDocumentSource({
                    sourceType: documentType,
                    fileName,
                    fileSizeBytes: Number(fileSizeBytes),
                    createdBy: "qa.architect"
                  });
                  setFileName("");
                  setFileSizeBytes("0");
                }}
              >
                Register Document
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
