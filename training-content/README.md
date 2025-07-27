# AWS Deep Dive Training Content

## Training Content Organization

This repository contains training materials organized into different pedagogical approaches ("lenses") for delivering AWS service training. All training approaches use the same underlying infrastructure but present content with different focus areas.

### 📁 Folder Structure

```
training-content/
├── financial-process-lens/     # Financial process implementation focus
├── aws-service-lens/          # AWS service capability focus
└── shared-resources/          # Common resources for all approaches
```

---

## Training Approaches

### 🏦 Financial Process Lens
**Focus**: Implementing financial business processes using AWS services
**Audience**: Finance professionals, compliance officers, business analysts
**Approach**: Prescriptive scenarios demonstrating specific financial workflows

**Key Materials**:
- `Manual-Deployment-Guide.md`: Comprehensive deployment with financial scenarios
- SOX compliance focus
- Financial process automation examples
- Regulatory compliance demonstrations

### ⚙️ AWS Service Lens  
**Focus**: Exploring AWS service capabilities and integration patterns
**Audience**: Cloud engineers, architects, developers
**Approach**: Discovery-based learning emphasizing service capabilities

**Key Materials**:
- `AWS-Service-Exploration-Guide.md`: Service-focused exploration activities
- `Training-Facilitator-Guide.md`: Facilitator instructions for hands-on workshops
- AWS native service capabilities emphasis
- Cross-service integration patterns

### 📚 Shared Resources
**Purpose**: Common infrastructure, deployment procedures, and troubleshooting
**Contains**: Templates, CLI commands, URLs, and troubleshooting guides
**Usage**: Referenced by all training approaches

---

## Infrastructure

**Single Unified Template**: `aws-deep-dive-training-unified.yaml`
- **Status**: Production-ready, fully tested
- **Services**: Lambda, Step Functions, EventBridge, Glue, CloudWatch, CloudTrail
- **Optimization**: Designed for training with frequent execution cycles

### Deployment
```bash
# Same deployment for all training approaches
aws cloudformation create-stack \
  --stack-name aws-deep-dive-training-stack \
  --template-body file://aws-deep-dive-training-unified.yaml \
  --parameters ParameterKey=EnvironmentName,ParameterValue=aws-deep-dive \
               ParameterKey=S3BucketName,ParameterValue=your-bucket-name \
  --capabilities CAPABILITY_IAM
```

---

## Choosing Your Training Approach

### Use Financial Process Lens When:
- ✅ Training finance or compliance teams
- ✅ Demonstrating specific business process automation
- ✅ SOX compliance requirements are important
- ✅ Participants need prescriptive, scenario-based learning
- ✅ Business process outcomes are the primary goal

### Use AWS Service Lens When:
- ✅ Training cloud engineers or developers
- ✅ Exploring AWS service capabilities and patterns
- ✅ Participants prefer discovery-based learning
- ✅ Cross-service integration understanding is important
- ✅ AWS service mastery is the primary goal

### Use Both Approaches When:
- ✅ Training mixed audiences (business + technical)
- ✅ Demonstrating business value AND technical implementation
- ✅ Creating comprehensive AWS training programs
- ✅ Building reusable training content for different audiences

---

## Content Reusability

**Same Infrastructure, Different Perspectives**:
- All training approaches use identical AWS infrastructure
- Content can be mixed and matched based on audience needs
- Facilitators can switch between lenses during training
- Participants get consistent hands-on experience

**Extensibility**:
- Add new training lenses without changing infrastructure
- Customize content for specific industries or use cases
- Scale from individual workshops to comprehensive programs

---

## Quick Start Guide

### For Financial Process Training:
1. Deploy infrastructure using unified template
2. Follow `financial-process-lens/Manual-Deployment-Guide.md`
3. Use SOX compliance scenarios and financial workflows
4. Reference `shared-resources/Common-Resources.md` for troubleshooting

### For AWS Service Training:
1. Deploy infrastructure using unified template  
2. Follow `aws-service-lens/AWS-Service-Exploration-Guide.md`
3. Use `aws-service-lens/Training-Facilitator-Guide.md` for workshop delivery
4. Reference `shared-resources/Common-Resources.md` for common procedures

### For Custom Training:
1. Deploy infrastructure using unified template
2. Combine elements from both lenses as needed
3. Use shared resources for consistent deployment and troubleshooting
4. Adapt content focus based on participant backgrounds

---

## Training Session Planning

### 2-Hour Workshop:
- **AWS Service Lens**: EventBridge + Lambda + CloudWatch
- **Financial Process Lens**: Transaction processing + compliance monitoring

### 4-Hour Workshop:
- **AWS Service Lens**: All services with hands-on exploration
- **Financial Process Lens**: Complete financial workflows + failure scenarios

### Full-Day Training:
- **Combined Approach**: Technical implementation + business process context
- **Multiple Lenses**: Different perspectives for different participant groups

---

## Maintenance and Updates

**Infrastructure Updates**:
- Modify `aws-deep-dive-training-unified.yaml` for technical changes
- Test changes with both training approaches
- Update shared resources documentation

**Content Updates**:
- Update specific lens folders for approach-specific changes
- Maintain cross-references in shared resources
- Version control ensures consistency across approaches

**Cost Optimization**:
- Training infrastructure optimized for workshop usage
- Built-in cleanup procedures
- Cost monitoring guidance in shared resources

---

## Contribution Guidelines

### Adding New Training Lenses:
1. Create new folder under `training-content/`
2. Follow naming convention: `[focus-area]-lens/`
3. Reference shared resources rather than duplicating content
4. Test with existing infrastructure
5. Update this README with new approach

### Modifying Existing Content:
1. Identify if change affects single lens or shared resources
2. Update appropriate folder(s)
3. Test changes with actual deployment
4. Verify cross-references remain valid

### Infrastructure Changes:
1. Modify unified template
2. Test with all existing training approaches
3. Update shared resources documentation
4. Verify cost implications

---

## Support and Troubleshooting

**Primary Reference**: `shared-resources/Common-Resources.md`

**Common Issues**:
- Infrastructure deployment problems
- Service permissions and access
- Dashboard data population
- Cost monitoring and cleanup

**Additional Support**:
- CloudFormation template includes comprehensive error handling
- All training materials include troubleshooting sections
- Facilitator guides include session-specific troubleshooting

This organized approach enables flexible, reusable AWS training content that can be adapted for different audiences while maintaining consistent infrastructure and shared resources.
