import CheckIcon from "@mui/icons-material/Check";
import CloseIcon from "@mui/icons-material/Close";
import EditIcon from "@mui/icons-material/Edit";
import SaveIcon from "@mui/icons-material/Save";
import {
  Chip,
  IconButton,
  Stack,
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableRow,
  TextField
} from "@mui/material";
import { useState } from "react";

import type { ReviewableItem } from "../types";

interface ReviewTableProps {
  items: ReviewableItem[];
  onReview: (
    item: ReviewableItem,
    action: "approve" | "reject" | "edit",
    payload?: { name?: string; description?: string }
  ) => Promise<void>;
}

function statusColor(status: ReviewableItem["status"]): "default" | "success" | "error" {
  if (status === "Approved") {
    return "success";
  }
  if (status === "Rejected") {
    return "error";
  }
  return "default";
}

export function ReviewTable({ items, onReview }: ReviewTableProps): JSX.Element {
  const [editId, setEditId] = useState<string | null>(null);
  const [name, setName] = useState("");
  const [description, setDescription] = useState("");

  return (
    <Table size="small">
      <TableHead>
        <TableRow>
          <TableCell>Name</TableCell>
          <TableCell>Description</TableCell>
          <TableCell>Status</TableCell>
          <TableCell>Approved By</TableCell>
          <TableCell align="right">Actions</TableCell>
        </TableRow>
      </TableHead>
      <TableBody>
        {items.map((item) => {
          const isEditing = editId === item.id;
          return (
            <TableRow key={item.id}>
              <TableCell sx={{ minWidth: 180 }}>
                {isEditing ? (
                  <TextField
                    value={name}
                    size="small"
                    fullWidth
                    onChange={(event) => setName(event.target.value)}
                  />
                ) : (
                  item.name
                )}
              </TableCell>
              <TableCell>
                {isEditing ? (
                  <TextField
                    value={description}
                    size="small"
                    fullWidth
                    onChange={(event) => setDescription(event.target.value)}
                  />
                ) : (
                  item.description
                )}
              </TableCell>
              <TableCell>
                <Chip size="small" label={item.status} color={statusColor(item.status)} />
              </TableCell>
              <TableCell>{item.approvedBy ?? "-"}</TableCell>
              <TableCell align="right">
                <Stack direction="row" justifyContent="flex-end" spacing={1}>
                  {isEditing ? (
                    <IconButton
                      size="small"
                      color="primary"
                      onClick={async () => {
                        await onReview(item, "edit", { name, description });
                        setEditId(null);
                      }}
                    >
                      <SaveIcon fontSize="small" />
                    </IconButton>
                  ) : (
                    <IconButton
                      size="small"
                      color="primary"
                      onClick={() => {
                        setEditId(item.id);
                        setName(item.name);
                        setDescription(item.description);
                      }}
                    >
                      <EditIcon fontSize="small" />
                    </IconButton>
                  )}
                  <IconButton
                    size="small"
                    color="success"
                    onClick={async () => onReview(item, "approve")}
                  >
                    <CheckIcon fontSize="small" />
                  </IconButton>
                  <IconButton
                    size="small"
                    color="error"
                    onClick={async () => onReview(item, "reject")}
                  >
                    <CloseIcon fontSize="small" />
                  </IconButton>
                </Stack>
              </TableCell>
            </TableRow>
          );
        })}
      </TableBody>
    </Table>
  );
}
