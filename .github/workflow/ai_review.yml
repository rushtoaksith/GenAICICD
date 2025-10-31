name: CI + AI Code Review

on:
  pull_request:
    types: [opened, synchronize, reopened]

jobs:
  test-and-ai-review:
    runs-on: ubuntu-latest
    steps:
    - name: Checkout code
      uses: actions/checkout@v4
      with:
        fetch-depth: 0  # get full history to compute diffs

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: "3.10"

    - name: Install deps
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt

    - name: Run tests
      run: |
        pytest -q

    - name: Save PR diff to file
      env:
        GITHUB_EVENT_PATH: ${{ github.event_path }}
      run: |
        # Save the git patch for the PR into a file
        git fetch origin ${{ github.base_ref }}:${{ github.base_ref }} || true
        git diff origin/${{ github.base_ref }}...HEAD > pr_diff.patch || true
        echo "=== DIFF START ==="
        head -n 50 pr_diff.patch || true
        echo "=== DIFF END ==="

    - name: Run AI Review
      env:
        OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
        GITHUB_TOKEN: ${{ secrets.GH_TOKEN }}
        PR_NUMBER: ${{ github.event.pull_request.number }}
        REPO: ${{ github.repository }}
      run: |
        python ai_review.py pr_diff.patch
