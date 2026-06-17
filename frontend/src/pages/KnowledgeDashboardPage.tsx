import { Alert, Card, CardContent, Grid, Stack, Typography } from "@mui/material";

import { ProjectSelector } from "../components/ProjectSelector";
import type { DashboardMetrics, Project } from "../types";

interface KnowledgeDashboardPageProps {
  projects: Project[];
  selectedProjectId: string;
  onSelectProject: (projectId: string) => void;
  metrics: DashboardMetrics | null;
}

function MetricCard({
  label,
  value
}: {
  label: string;
  value: string | number;
}): JSX.Element {
  return (
    <Card>
      <CardContent>
        <Typography variant="caption" color="text.secondary">
          {label}
        </Typography>
        <Typography variant="h4">{value}</Typography>
      </CardContent>
    </Card>
  );
}

export function KnowledgeDashboardPage({
  projects,
  selectedProjectId,
  onSelectProject,
  metrics
}: KnowledgeDashboardPageProps): JSX.Element {
  return (
    <Stack spacing={3}>
      <Typography variant="h4">Knowledge Dashboard</Typography>
      <ProjectSelector
        projects={projects}
        selectedProjectId={selectedProjectId}
        onSelect={onSelectProject}
      />
      {!selectedProjectId ? <Alert severity="info">Select a project to view metrics.</Alert> : null}
      {!metrics && selectedProjectId ? (
        <Alert severity="warning">Generate a knowledge base to populate dashboard metrics.</Alert>
      ) : null}
      {metrics ? (
        <>
          <Grid container spacing={2}>
            <Grid size={{ xs: 6, md: 2 }}>
              <MetricCard label="Feature Count" value={metrics.featureCount} />
            </Grid>
            <Grid size={{ xs: 6, md: 2 }}>
              <MetricCard label="Domain Count" value={metrics.domainCount} />
            </Grid>
            <Grid size={{ xs: 6, md: 2 }}>
              <MetricCard label="Rule Count" value={metrics.ruleCount} />
            </Grid>
            <Grid size={{ xs: 6, md: 2 }}>
              <MetricCard label="Flow Count" value={metrics.flowCount} />
            </Grid>
            <Grid size={{ xs: 12, md: 4 }}>
              <MetricCard label="Approval Percentage" value={`${metrics.approvalPercentage}%`} />
            </Grid>
          </Grid>
          <Card>
            <CardContent>
              <Typography variant="h6" gutterBottom>
                Coverage Metrics
              </Typography>
              {Object.entries(metrics.coverageMetrics).map(([key, value]) => (
                <Typography key={key} variant="body1">
                  {key}: {value}
                </Typography>
              ))}
            </CardContent>
          </Card>
        </>
      ) : null}
    </Stack>
  );
}
