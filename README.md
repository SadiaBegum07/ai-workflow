# AI WORKFLOW CAPSTONE PROJECT

This project is part of the Coursera **AI Workflow Capstone**.  
It demonstrates how to use the AI development workflow to deploy a simple business solution using Python and FastAPI.

---

## 🚀 Project Overview
This app provides a **Matrix Multiplication API** where users can multiply two 2x2 matrices through a REST endpoint.

### Example:
`/multiply?a11=1&a12=2&a21=3&a22=4&b11=5&b12=6&b21=7&b22=8`

Output:
```json
{
  "matrix_A": [[1, 2], [3, 4]],
  "matrix_B": [[5, 6], [7, 8]],
  "result": [[19, 22], [43, 50]]
}
