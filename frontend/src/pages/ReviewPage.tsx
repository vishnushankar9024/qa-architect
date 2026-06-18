import { Alert, Card, CardContent, Stack, Typography } from "@mui/material";

import { ProjectSelector } from "../components/ProjectSelector";
import { ReviewTable } from "../components/ReviewTable";
import type { Project, ReviewableItem } from "../types";

interface ReviewPageProps {
  title: string;
  projects: Project[];
  selectedProjectId: string;
  onSelectProject: (projectId: string) => void;
  items: ReviewableItem[];
  onReview: (
    item: ReviewableItem,
    action: "approve" | "reject" | "edit",
    payload?: { name?: string; description?: string }
  ) => Promise<void>;
}

export function ReviewPage({
  title,
  projects,
  selectedProjectId,
  onSelectProject,
  items,
  onReview
}: ReviewPageProps) {
  return (
    <Stack spacing={3}>
      <Typography variant="h4">{title}</Typography>
      <ProjectSelector
        projects={projects}
        selectedProjectId={selectedProjectId}
        onSelect={onSelectProject}
      />
      {!selectedProjectId ? (
        <Alert severity="info">Select a project to review generated artifacts.</Alert>
      ) : null}
      {selectedProjectId && items.length === 0 ? (
        <Alert severity="warning">Generate knowledge base data before review.</Alert>
      ) : null}
      {items.length > 0 ? (
        <Card>
          <CardContent>
            <ReviewTable items={items} onReview={onReview} />
          </CardContent>
        </Card>
      ) : null}
    </Stack>
  );
}
