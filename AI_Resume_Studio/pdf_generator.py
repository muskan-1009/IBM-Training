from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from io import BytesIO


def create_pdf(title, content):
    """
    Generates a PDF from the given title and content.
    Returns PDF as bytes.
    """

    buffer = BytesIO()

    doc = SimpleDocTemplate(buffer)

    styles = getSampleStyleSheet()

    story = []

    # Title
    story.append(Paragraph(f"<b>{title}</b>", styles["Title"]))

    story.append(Paragraph("<br/><br/>", styles["Normal"]))

    # Split content into paragraphs
    for line in content.split("\n"):

        if line.strip():
            story.append(Paragraph(line, styles["BodyText"]))

    doc.build(story)

    pdf = buffer.getvalue()

    buffer.close()

    return pdf