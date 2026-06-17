import DescriptionIcon from "@mui/icons-material/Description";
import DomainIcon from "@mui/icons-material/Domain";
import FolderIcon from "@mui/icons-material/Folder";
import HubIcon from "@mui/icons-material/Hub";
import RuleIcon from "@mui/icons-material/Rule";
import SourceIcon from "@mui/icons-material/Source";
import UploadFileIcon from "@mui/icons-material/UploadFile";
import ViewTimelineIcon from "@mui/icons-material/ViewTimeline";
import {
  AppBar,
  Box,
  Container,
  Drawer,
  List,
  ListItemButton,
  ListItemIcon,
  ListItemText,
  Toolbar,
  Typography
} from "@mui/material";
import { NavLink } from "react-router-dom";

const drawerWidth = 260;

const navItems = [
  { label: "Projects", to: "/", icon: <FolderIcon /> },
  { label: "Knowledge Sources", to: "/sources", icon: <SourceIcon /> },
  { label: "Knowledge Dashboard", to: "/dashboard", icon: <HubIcon /> },
  { label: "Features", to: "/features", icon: <DescriptionIcon /> },
  { label: "Domains", to: "/domains", icon: <DomainIcon /> },
  { label: "Business Rules", to: "/business-rules", icon: <RuleIcon /> },
  { label: "Flows", to: "/flows", icon: <ViewTimelineIcon /> },
  { label: "Exports", to: "/exports", icon: <UploadFileIcon /> }
];

export function AppLayout({ children }: { children: React.ReactNode }) {
  return (
    <Box sx={{ display: "flex", minHeight: "100vh", bgcolor: "grey.100" }}>
      <AppBar position="fixed" sx={{ zIndex: (theme) => theme.zIndex.drawer + 1 }}>
        <Toolbar>
          <Typography variant="h6" noWrap>
            QA Architect Portal v1
          </Typography>
        </Toolbar>
      </AppBar>
      <Drawer
        variant="permanent"
        sx={{
          width: drawerWidth,
          flexShrink: 0,
          [`& .MuiDrawer-paper`]: { width: drawerWidth, boxSizing: "border-box" }
        }}
      >
        <Toolbar />
        <List>
          {navItems.map((item) => (
            <ListItemButton
              key={item.to}
              component={NavLink}
              to={item.to}
              sx={{
                "&.active": {
                  bgcolor: "primary.light",
                  color: "primary.contrastText",
                  "& .MuiListItemIcon-root": { color: "primary.contrastText" }
                }
              }}
            >
              <ListItemIcon>{item.icon}</ListItemIcon>
              <ListItemText primary={item.label} />
            </ListItemButton>
          ))}
        </List>
      </Drawer>
      <Box component="main" sx={{ flexGrow: 1, p: 3 }}>
        <Toolbar />
        <Container maxWidth="xl">{children}</Container>
      </Box>
    </Box>
  );
}
