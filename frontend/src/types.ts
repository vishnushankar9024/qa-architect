export type ProjectStatus = "Draft" | "Knowledge Generation" | "Review" | "Approved";

export interface Project {
  id: string;
  name: string;
  description: string;
  createdBy: string;
  createdDate: string;
  status: ProjectStatus;
}

export interface KnowledgeSource {
  id: string;
  projectId: string;
  sourceType: string;
  status: "Uploaded" | "Processing" | "Completed" | "Failed";
  createdBy: string;
  createdDate: string;
  metadata: Record<string, string | number>;
}

export interface ReviewableItem {
  id: string;
  name: string;
  description: string;
  status: "Pending" | "Approved" | "Rejected";
  approvedBy: string | null;
  approvedDate: string | null;
}

export interface TraceabilityItem {
  id: string;
  source: string;
  target: string;
  status: "Pending" | "Approved" | "Rejected";
  approvedBy: string | null;
  approvedDate: string | null;
}

export interface KnowledgeBase {
  project: Record<string, string>;
  features: ReviewableItem[];
  domains: ReviewableItem[];
  flows: ReviewableItem[];
  business_rules: ReviewableItem[];
  traceability: TraceabilityItem[];
}

export interface DashboardMetrics {
  featureCount: number;
  domainCount: number;
  ruleCount: number;
  flowCount: number;
  approvalPercentage: number;
  coverageMetrics: Record<string, number>;
}
