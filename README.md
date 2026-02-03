# CodeWars Solutions

This repository contains my solutions to various CodeWars problems implemented in multiple programming languages.

## Languages Supported

- TypeScript
- JavaScript
- C#
- Python

## Project Structure

```
Solutions/
  {Problem_Name}/
    TS/
      solution.ts
      solution.test.ts
    JS/
      solution.js
      solution.test.js
    CS/
      Solution.cs
      SolutionTests.cs
    PY/
      solution.py
      solution_test.py
```

## Running Tests

**Important:** All commands must be run from the root directory (`codeWars-solutions/`)

#### JavaScript/TypeScript Tests

```bash
npm test
```

#### C# Tests

```bash
dotnet test --filter "FullyQualifiedName~Solutions.{FOLDER_NAME}.CS"
```

#### Python Tests

```bash
pytest
```

## Setup

### Prerequisites

- Node.js (for JavaScript/TypeScript)
- .NET 9.0 SDK (for C#)
- Python 3.x (for Python)

### Installation

1. Clone the repository
2. **Navigate to the project root:**
   ```bash
   cd codeWars-solutions
   ```
3. Install JavaScript/TypeScript dependencies:
   ```bash
   npm install
   ```
4. Restore C# packages:
   ```bash
   dotnet restore
   ```
