import sys
import os
import logging
import uuid
import shutil
from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from fastapi.responses import JSONResponse

# Extend path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

# Internal imports
from ux2ui.prompts_bundle.generateHTML import *
from ux2ui.utils.post_processing import *
from ux2ui.features.chat2modify.chat2modify import *

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("ux2ui_app.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

# FastAPI app
app = FastAPI()

UPLOAD_DIR = "temp_uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@app.post("/generateHTML/")
async def generateHtml(
    file: UploadFile = File(...),
    app_name: str = Form("demo")
):
    try:
        logger.info(f"Received upload request for app: {app_name}, file: {file.filename}")

        # Save uploaded file temporarily
        ext = os.path.splitext(file.filename)[-1]
        unique_filename = f"{uuid.uuid4().hex}{ext}"
        image_path = os.path.join(UPLOAD_DIR, unique_filename)

        with open(image_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        logger.info(f"Saved uploaded image to: {image_path}")

        # Step 1: Generate HTML
        html_code = generateHTML(image_path)
        logger.info("Generated HTML from image")

        # Step 2: Parse HTML
        parse_html(html_code, app_name)
        logger.info("Parsed HTML")

        # Step 3: Explain HTML
        explanation = explanationHTML(html_code)
        logger.info("Generated explanation for HTML")

        # Optional cleanup
        os.remove(image_path)
        logger.info("Deleted temporary file")

        return JSONResponse(content={
            "app_name": app_name,
            "html_code": html_code,
            "explanation": explanation
        })

    except Exception as e:
        logger.exception("Error during UX processing")
        raise HTTPException(status_code=500, detail=f"Processing failed: {str(e)}")


@app.post("/modifyHTML/")
async def generateHtml(
    query: str = Form("change bg to black"),
    app_name: str = Form("demo")
):
    try:
        logger.info(f"Received user {query}")

        html_code = read_html(app_name)

        # Step 1: Generate HTML
        modify_html_code = modifyHTML(query,app_name)
        logger.info(f"Generated HTML based on query: {query}")

        # Step 2: Parse HTML
        parse_html(html_code, app_name)
        logger.info("Parsed HTML")

        # Step 3: Explain HTML
        explanation = explanationHTML_changes(html_code,modify_html_code, query )
        logger.info("Generated explanation for HTML")


        return JSONResponse(content={
            "app_name": app_name,
            "html_code": html_code,
            "explanation": explanation
        })

    except Exception as e:
        logger.exception("Error during UX processing")
        raise HTTPException(status_code=500, detail=f"Processing failed: {str(e)}")

