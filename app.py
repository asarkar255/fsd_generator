from fastapi import FastAPI, UploadFile, Form
from .fsd_generator import generate_fsd
from formatter import fsd_to_docx

app = FastAPI()

@app.post("/generate_fsd/")
async def generate_fsd_api(abap_code: str = Form(...)):
    fsd = generate_fsd(abap_code)
    if "error" in fsd:
        return fsd
    filename = fsd_to_docx(fsd)
    return {"fsd": fsd, "docx_file": filename}
