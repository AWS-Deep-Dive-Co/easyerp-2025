# easyerp

Enterprise Resource Planning System with Django and AWS deployment.

## Deployment Notes

### Certificate Generation
```bash
sudo certbot certonly --manual --preferred-challenges dns
```

## ECS Execute Command Setup

To enable shell access into running ECS containers for debugging and maintenance.

### Prerequisites
- ECS service must be running
- ECSTaskExecutionRole must have SSM permissions (already configured in infrastructure)
- AWS CLI configured with appropriate permissions

### Step 1: Enable Execute Command on Service
```bash
aws ecs update-service \
  --cluster CLUSTER_NAME \
  --service SERVICE_NAME \
  --region REGION \
  --enable-execute-command \
  --force-new-deployment
```

### Step 2: Get Task ARN
This assumes only 1 task is running for the service. If multiple tasks exist, manually get the ARN from ECS console.

```bash
TASK_ARN=$(aws ecs list-tasks \
  --cluster CLUSTER_NAME \
  --service SERVICE_NAME \
  --region REGION \
  --output text \
  --query 'taskArns[0]')
```

### Step 3: Verify Task Details (Optional)
```bash
aws ecs describe-tasks \
  --cluster CLUSTER_NAME \
  --region REGION \
  --tasks $TASK_ARN
```

### Step 4: Execute Shell Command
```bash
aws ecs execute-command \
  --region REGION \
  --cluster CLUSTER_NAME \
  --task $TASK_ARN \
  --container CONTAINER_NAME \
  --command "sh" \
  --interactive
```

### Environment Variables
For easier usage, set these environment variables:

**Linux/Mac:**
```bash
export CLUSTER_NAME="your-cluster-name"
export SERVICE_NAME="your-service-name"
export REGION="us-east-2"
export CONTAINER_NAME="easyerp"
```

**Windows (PowerShell):**
```powershell
$env:CLUSTER_NAME="your-cluster-name"
$env:SERVICE_NAME="your-service-name"
$env:REGION="us-east-2"
$env:CONTAINER_NAME="easyerp"
```

**Windows (Command Prompt):**
```cmd
set CLUSTER_NAME=your-cluster-name
set SERVICE_NAME=your-service-name
set REGION=us-east-2
set CONTAINER_NAME=easyerp
```

Then use:

**Linux/Mac:**
```bash
# Enable execute command
aws ecs update-service --cluster $CLUSTER_NAME --service $SERVICE_NAME --region $REGION --enable-execute-command --force-new-deployment

# Get task ARN
TASK_ARN=$(aws ecs list-tasks --cluster $CLUSTER_NAME --service $SERVICE_NAME --region $REGION --output text --query 'taskArns[0]')

# Execute command
aws ecs execute-command --region $REGION --cluster $CLUSTER_NAME --task $TASK_ARN --container $CONTAINER_NAME --command "sh" --interactive
```

**Windows (PowerShell):**
```powershell
# Enable execute command
aws ecs update-service --cluster $env:CLUSTER_NAME --service $env:SERVICE_NAME --region $env:REGION --enable-execute-command --force-new-deployment

# Get task ARN
$TASK_ARN = aws ecs list-tasks --cluster $env:CLUSTER_NAME --service $env:SERVICE_NAME --region $env:REGION --output text --query 'taskArns[0]'

# Execute command
aws ecs execute-command --region $env:REGION --cluster $env:CLUSTER_NAME --task $TASK_ARN --container $env:CONTAINER_NAME --command "sh" --interactive
```

**Windows (Command Prompt):**
```cmd
# Enable execute command
aws ecs update-service --cluster %CLUSTER_NAME% --service %SERVICE_NAME% --region %REGION% --enable-execute-command --force-new-deployment

# Get task ARN (Note: You'll need to manually copy the ARN from the output)
aws ecs list-tasks --cluster %CLUSTER_NAME% --service %SERVICE_NAME% --region %REGION% --output text --query "taskArns[0]"

# Execute command (replace TASK_ARN_HERE with the actual ARN from above)
aws ecs execute-command --region %REGION% --cluster %CLUSTER_NAME% --task TASK_ARN_HERE --container %CONTAINER_NAME% --command "sh" --interactive
```

### Troubleshooting
- Ensure the service has `enableExecuteCommand` set to `true`
- Verify the task role has the required SSM permissions
- Check that the container is running and healthy
- Use `aws ecs describe-tasks` to verify task status

---

JK added a new feature 7/28/2025
