### Contribution Guidelines

- Process Flow:<br /><br />
![flow-chart.jpg](img%2Fflow-chart.jpg)
- GitLab Pipeline Flow:<br /><br />
![pipeline.PNG](img%2Fpipeline.PNG)
- Clone Repository:
    ```bash
    # Clone the repository
    git clone <repository_url>
    
    # Navigate into the project directory
    cd unified-automation-framework
    
    # Create a feature branch
    git checkout -b feature/<branch_name>
    
    # Make your changes to the code
    
    # Add changes to staging
    git add .
    
    # Commit changes
    git commit -m "Description of changes"
    
    # Push feature branch to remote
    git push origin feature/<branch_name>
    ```
- Create Merge Request:
  1. Go to your project on GitLab.Click on "Merge Requests."
  2. Click on "New Merge Request."
  3. Select the source branch (your feature branch) and the target branch (main). 
  4. Click on "Compare branches and continue."
  5. Fill in the details and click on "Create merge request."

- Code Review and Merge:
  1. Reviewers will review the code and provide feedback. 
  2. Once approved, the merge request can be merged to the main branch.

