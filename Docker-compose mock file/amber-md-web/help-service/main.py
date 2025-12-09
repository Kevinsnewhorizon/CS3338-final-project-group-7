from fastapi import FastAPI

app = FastAPI()

@app.get("/help")
def help_root():
    return {
        "Amber Tips": [
            "Use pmemd.cuda for GPU runs",
            "Minimize before production MD",
            "Check periodic box and restraints carefully",
            "Use cpptraj for trajectory post-processing"
        ]
    }
