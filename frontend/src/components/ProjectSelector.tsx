import { FormControl, InputLabel, MenuItem, Select } from "@mui/material";

import type { Project } from "../types";

interface ProjectSelectorProps {
  projects: Project[];
  selectedProjectId: string;
  onSelect: (projectId: string) => void;
}

export function ProjectSelector({
  projects,
  selectedProjectId,
  onSelect
}: ProjectSelectorProps): JSX.Element {
  return (
    <FormControl fullWidth size="small">
      <InputLabel id="project-select-label">Project</InputLabel>
      <Select
        labelId="project-select-label"
        label="Project"
        value={selectedProjectId}
        onChange={(event) => onSelect(event.target.value)}
      >
        {projects.map((project) => (
          <MenuItem key={project.id} value={project.id}>
            {project.name} ({project.status})
          </MenuItem>
        ))}
      </Select>
    </FormControl>
  );
}
