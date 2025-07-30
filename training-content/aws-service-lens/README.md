# AWS Services Training Content Organization

This folder contains all training materials for the AWS Services for Auditors course, organized into logical categories for easy navigation and use.

## Folder Structure

### 📁 01-general-training-materials/
**Purpose**: Core training content used throughout the course
**Contents**:
- `PowerPoint-Slide-Layout.md` - Complete slide deck with voiceover notes (19 slides)
- `AWS-Service-Exploration-Guide.md` - Comprehensive guide to AWS services from audit perspective

**Usage**: Primary training materials for instructor-led sessions

---

### 📁 02-hands-on-activities/
**Purpose**: Individual and small group hands-on exercises
**Contents**:
- `Activity-1-EventBridge-Analysis.md` - EventBridge and CloudWatch exploration (10 minutes)
- `Activity-2-Workflow-Risk-Assessment.md` - Step Functions and Glue workflow analysis (10 minutes)  
- `Activity-3-Compliance-Evidence-Gathering.md` - Comprehensive monitoring and evidence collection (10 minutes)

**Usage**: Structured activities for participants to complete independently or in small groups

---

### 📁 03-live-demo-materials/
**Purpose**: Materials for the live mock audit walkthrough demonstration
**Contents**:
- `Activity-Live-Demo-Change-Management-SOD.md` - Main activity guide for change management and SOD controls audit
- `Architecture-Diagram-Audit-Evidence-Map.md` - Architecture diagrams and evidence location maps
- `Mock-Team-Accounts-Access-Matrix.md` - Complete team structure with access violations (facilitator version)
- `Participant-Team-Access-Review-Guide.md` - Participant-facing team access review guide

**Usage**: Interactive demonstration where facilitator acts as DevOps lead and participants audit the environment

---

### 📁 04-facilitator-resources/
**Purpose**: Setup guides and preparation materials for instructors
**Contents**:
- `Training-Facilitator-Guide.md` - Master facilitator guide with timing, transitions, and teaching notes
- `Facilitator-Preparation-Checklist.md` - Step-by-step setup guide for easter eggs and access violations
- `Implementation-Guide-Mock-Accounts.md` - Technical implementation guide for creating mock accounts and violations

**Usage**: Behind-the-scenes materials for course preparation and delivery

---

## Training Flow Overview

### **Part 1: Foundation (60 minutes)**
- Use materials from `01-general-training-materials/`
- PowerPoint presentation with live AWS console demonstrations
- Establishes monitoring foundation and service understanding

### **Part 2: Hands-On Practice (30 minutes)**
- Use materials from `02-hands-on-activities/`
- Three 10-minute individual/group activities
- Builds practical AWS console navigation skills

### **Part 3: Live Mock Audit (45 minutes)**
- Use materials from `03-live-demo-materials/`
- Interactive audit simulation with real control weaknesses
- Participants discover and document access violations

## Quick Start Guide for Facilitators

### **First Time Setup**:
1. Review `04-facilitator-resources/Training-Facilitator-Guide.md`
2. Complete `04-facilitator-resources/Facilitator-Preparation-Checklist.md`
3. Set up AWS environment using `04-facilitator-resources/Implementation-Guide-Mock-Accounts.md`

### **Before Each Training**:
1. Print `03-live-demo-materials/Participant-Team-Access-Review-Guide.md` for participants
2. Test AWS console access and GitHub repository access
3. Review easter eggs and hidden violations
4. Prepare architecture diagram presentation

### **During Training**:
1. Start with `01-general-training-materials/PowerPoint-Slide-Layout.md`
2. Proceed through `02-hands-on-activities/` in sequence
3. Conclude with `03-live-demo-materials/Activity-Live-Demo-Change-Management-SOD.md`

## File Naming Convention

- **Activity-[Number]-[Topic].md**: Structured hands-on exercises
- **[Topic]-Guide.md**: Comprehensive guides and resources
- **[Audience]-[Purpose].md**: Role-specific materials (Facilitator, Participant)

## Content Updates

When updating materials:
- Maintain consistency across all files in the same category
- Update the main facilitator guide when adding new activities
- Test all hands-on activities in the training AWS environment
- Keep participant guides free of spoilers and implementation details

---

**Total Training Duration**: 2 hours and 15 minutes
**Recommended Class Size**: 8-12 participants
**Prerequisites**: Basic understanding of auditing concepts, no AWS experience required
