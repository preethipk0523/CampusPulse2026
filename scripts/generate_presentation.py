"""
Generate a professional, high-impact PowerPoint presentation (.pptx)
for CampusPulse 2026 that strictly fits a 10-minute presentation.
Includes native vector architecture shapes on Slide 3 with clear separation
between deployed components and Proposed Future Enhancements (Not Implemented).
"""
import sys
from pathlib import Path
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def build_presentation():
    prs = Presentation()
    # 16:9 Widescreen layout
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Color Palette
    BG_DARK = RGBColor(15, 23, 42)       # #0f172a Deep Slate
    CARD_BG = RGBColor(30, 41, 59)       # #1e293b Slate 800
    CARD_BORDER = RGBColor(51, 65, 85)   # #334155 Slate 700
    TEXT_LIGHT = RGBColor(248, 250, 252) # #f8fafc
    TEXT_MUTED = RGBColor(148, 163, 184) # #94a3b8
    ACCENT_BLUE = RGBColor(56, 189, 248) # #38bdf8 Cyan
    ACCENT_ORANGE = RGBColor(249, 115, 22) # #f97316 Orange
    ACCENT_GREEN = RGBColor(74, 222, 128)  # #4ade80 Green
    ACCENT_YELLOW = RGBColor(250, 204, 21) # #facc15 Amber
    ACCENT_PURPLE = RGBColor(168, 85, 247) # #a855f7 Purple
    FUTURE_BG = RGBColor(24, 24, 27)     # #18181b Zinc 900
    FUTURE_BORDER = RGBColor(202, 138, 4) # Amber border

    def set_slide_background(slide):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = BG_DARK
        bg.line.fill.background()
        return bg

    def add_header(slide, title_text, subtitle_text="CampusPulse 2026 | AWS eu-west-3 (Paris)"):
        # Header banner
        header = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.7), Inches(0.9))
        tf = header.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
        
        p = tf.paragraphs[0]
        p.text = title_text
        p.font.size = Pt(24)
        p.font.bold = True
        p.font.color.rgb = TEXT_LIGHT

        p2 = tf.add_paragraph()
        p2.text = subtitle_text
        p2.font.size = Pt(11)
        p2.font.color.rgb = ACCENT_BLUE

    def add_notes(slide, notes_text):
        notes_slide = slide.notes_slide
        tf = notes_slide.notes_text_frame
        tf.text = notes_text

    # ==========================================
    # SLIDE 1: TITLE SLIDE (0:00 - 1:00)
    # ==========================================
    s1 = prs.slides.add_slide(blank_layout)
    set_slide_background(s1)

    # Title Card Box
    card = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.5), Inches(1.2), Inches(10.333), Inches(5.1))
    card.fill.solid()
    card.fill.fore_color.rgb = CARD_BG
    card.line.color.rgb = CARD_BORDER
    card.line.width = Pt(1.5)

    tf = card.text_frame
    tf.word_wrap = True
    tf.margin_top = Inches(0.6)
    tf.margin_left = Inches(0.8)

    p = tf.paragraphs[0]
    p.text = "CampusPulse 2026"
    p.font.size = Pt(36)
    p.font.bold = True
    p.font.color.rgb = TEXT_LIGHT

    p2 = tf.add_paragraph()
    p2.text = "Cloud-Native Smart Campus Operations Platform"
    p2.font.size = Pt(20)
    p2.font.color.rgb = ACCENT_BLUE
    p2.space_before = Pt(8)

    p3 = tf.add_paragraph()
    p3.text = "Module: Big Data & Cloud Computing | Academic Year 2025–2026"
    p3.font.size = Pt(13)
    p3.font.color.rgb = TEXT_MUTED
    p3.space_before = Pt(24)

    p4 = tf.add_paragraph()
    p4.text = "Cloud Provider: Amazon Web Services (AWS) | Region: Paris (eu-west-3)"
    p4.font.size = Pt(13)
    p4.font.color.rgb = TEXT_MUTED
    p4.space_before = Pt(6)

    p5 = tf.add_paragraph()
    p5.text = "Project Team: Joswikkha Dilli Babu  •  Preethi Krishnamoorthi  •  Anbuselvan Ponnusamy"
    p5.font.size = Pt(14)
    p5.font.bold = True
    p5.font.color.rgb = ACCENT_GREEN
    p5.space_before = Pt(28)

    add_notes(s1, "Time: 1 min (0:00 - 1:00)\nSpeaker Notes: Good morning/afternoon everyone. Today we are presenting CampusPulse 2026, our cloud-native smart campus operations platform. CampusPulse was designed and deployed on AWS in the Paris region (eu-west-3). It provides a serverless pipeline for ingesting simulated campus telemetry, storing records persistently in DynamoDB, calculating real-time facility metrics, and detecting operational alerts. Presented by Joswikkha, Preethi, and Anbuselvan.")

    # ==========================================
    # SLIDE 2: OBJECTIVES & PROBLEM (1:00 - 2:00)
    # ==========================================
    s2 = prs.slides.add_slide(blank_layout)
    set_slide_background(s2)
    add_header(s2, "1. Project Objectives & Operational Scope")

    # 3 Cards side by side
    col_w = Inches(3.64)
    gap = Inches(0.38)
    top_y = Inches(1.6)
    card_h = Inches(5.2)

    cards_data = [
        ("The Challenge", ACCENT_ORANGE, [
            "Campus facilities generate continuous telemetry (occupancy, energy, temperature).",
            "Manual logs and disparate sensors lead to delayed anomaly detection and wasted energy.",
            "Requirement: A lightweight, event-driven, cost-conscious ingestion & monitoring pipeline."
        ]),
        ("Core Objectives", ACCENT_BLUE, [
            "Deploy a cloud-hosted REST API with public & protected endpoints in AWS eu-west-3.",
            "Ingest simulated JSON event streams using Python automation.",
            "Validate data integrity, compute live operations statistics, and classify alerts.",
            "Enforce role-based access control (Admin & Operator roles) with least privilege IAM."
        ]),
        ("Success Criteria", ACCENT_GREEN, [
            "100% serverless: Zero provisioned server instances, pay-per-request billing.",
            "High test coverage: Automated Python unit tests verifying edge cases and business rules.",
            "Full observability: Real-time CloudWatch execution logs for audit and diagnostics."
        ])
    ]

    for i, (title, accent, bullets) in enumerate(cards_data):
        cx = Inches(0.8) + i * (col_w + gap)
        box = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, cx, top_y, col_w, card_h)
        box.fill.solid()
        box.fill.fore_color.rgb = CARD_BG
        box.line.color.rgb = CARD_BORDER
        box.line.width = Pt(1.5)

        tf = box.text_frame
        tf.word_wrap = True
        tf.margin_top = Inches(0.3)
        tf.margin_left = Inches(0.3)
        tf.margin_right = Inches(0.3)

        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(16)
        p.font.bold = True
        p.font.color.rgb = accent

        for b in bullets:
            pb = tf.add_paragraph()
            pb.text = "• " + b
            pb.font.size = Pt(12)
            pb.font.color.rgb = TEXT_LIGHT
            pb.space_before = Pt(12)

    add_notes(s2, "Time: 1 min (1:00 - 2:00)\nSpeaker Notes: Why CampusPulse? Modern universities manage dozens of buildings. When a lab overheats or room occupancy surges, campus staff need immediate visibility without running expensive dedicated servers 24/7. Our primary goals were to create a working AWS serverless architecture deployed via SAM, accept simulated event streams, validate metrics against strict thresholds, persist them to DynamoDB, and demonstrate clear role separation.")

    # ==========================================
    # SLIDE 3: ARCHITECTURE (2:00 - 3:30)
    # ==========================================
    s3 = prs.slides.add_slide(blank_layout)
    set_slide_background(s3)
    add_header(s3, "2. System Architecture: Verified Live vs Proposed Future")

    # Section 1 Box (Deployed)
    d_box = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.5), Inches(11.733), Inches(3.4))
    d_box.fill.solid()
    d_box.fill.fore_color.rgb = CARD_BG
    d_box.line.color.rgb = RGBColor(22, 101, 52)
    d_box.line.width = Pt(1.5)

    # Section 1 Tag
    tag1 = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0), Inches(1.65), Inches(3.2), Inches(0.35))
    tag1.fill.solid()
    tag1.fill.fore_color.rgb = RGBColor(22, 101, 52)
    tag1.line.fill.background()
    p = tag1.text_frame.paragraphs[0]
    p.text = "VERIFIED LIVE ARCHITECTURE (DEPLOYED)"
    p.font.size = Pt(10)
    p.font.bold = True
    p.font.color.rgb = TEXT_LIGHT
    p.alignment = PP_ALIGN.CENTER

    # 4 Deployed Architecture Boxes
    arch_nodes = [
        ("Client / Ingestion", Inches(1.0), Inches(2.2), Inches(2.4), Inches(2.4), ACCENT_PURPLE,
         ["generate_events.py", "REST Clients / PS", "TLS 1.2+ HTTPS", "Admin & Operator"]),
        ("Amazon API Gateway", Inches(3.9), Inches(2.2), Inches(2.6), Inches(2.4), ACCENT_BLUE,
         ["REST API (prod)", "GET /health (Public)", "POST /login (Auth)", "GET & POST /events", "GET /stats, /alerts"]),
        ("AWS Lambda Function", Inches(7.0), Inches(2.2), Inches(2.6), Inches(2.4), ACCENT_ORANGE,
         ["Python 3.12 | 256MB", "Validation logic", "Threshold classification", "Latest room occupancy", "IAM Execution Role"]),
        ("Amazon DynamoDB", Inches(10.1), Inches(2.2), Inches(2.2), Inches(2.4), ACCENT_GREEN,
         ["CampusPulseEvents", "PK: event_id (S)", "PAY_PER_REQUEST", "Attributes: occ, temp,", "energy, severity, time"])
    ]

    for title, x, y, w, h, col, lines in arch_nodes:
        node = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, w, h)
        node.fill.solid()
        node.fill.fore_color.rgb = RGBColor(15, 23, 42)
        node.line.color.rgb = col
        node.line.width = Pt(1.2)
        tf = node.text_frame
        tf.word_wrap = True
        tf.margin_top = Inches(0.15)
        tf.margin_left = Inches(0.15)
        
        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(12)
        p.font.bold = True
        p.font.color.rgb = col

        for ln in lines:
            pl = tf.add_paragraph()
            pl.text = "• " + ln
            pl.font.size = Pt(9.5)
            pl.font.color.rgb = TEXT_LIGHT
            pl.space_before = Pt(3)

    # Section 2 Box: Proposed Future Enhancements (NOT IMPLEMENTED)
    f_box = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(5.1), Inches(11.733), Inches(1.9))
    f_box.fill.solid()
    f_box.fill.fore_color.rgb = FUTURE_BG
    f_box.line.color.rgb = FUTURE_BORDER
    f_box.line.width = Pt(1.5)

    tag2 = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0), Inches(5.2), Inches(4.5), Inches(0.32))
    tag2.fill.solid()
    tag2.fill.fore_color.rgb = RGBColor(133, 77, 14)
    tag2.line.fill.background()
    p = tag2.text_frame.paragraphs[0]
    p.text = "PROPOSED FUTURE ENHANCEMENTS — NOT IMPLEMENTED"
    p.font.size = Pt(10)
    p.font.bold = True
    p.font.color.rgb = RGBColor(254, 249, 195)
    p.alignment = PP_ALIGN.CENTER

    # 4 future modules
    f_modules = [
        ("1. Production Identity", ["Amazon Cognito User Pools", "OAuth2 / JWT Authorizers"]),
        ("2. Web UI & CDN", ["React/Next.js Dashboard", "Amazon S3 + CloudFront CDN"]),
        ("3. VPC & Secrets", ["Private Subnets & VPC Endpoints", "AWS Secrets Manager"]),
        ("4. Automated DR & Push", ["DynamoDB PITR & AWS Backup", "CloudWatch Alarms + SNS SMS"])
    ]
    for i, (mtitle, mlines) in enumerate(f_modules):
        mx = Inches(1.0) + i * Inches(2.85)
        mbox = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, mx, Inches(5.6), Inches(2.7), Inches(1.25))
        mbox.fill.solid()
        mbox.fill.fore_color.rgb = RGBColor(15, 23, 42)
        mbox.line.color.rgb = FUTURE_BORDER
        mbox.line.width = Pt(1.0)
        tf = mbox.text_frame
        tf.word_wrap = True
        tf.margin_top = Inches(0.1)
        tf.margin_left = Inches(0.12)
        p = tf.paragraphs[0]
        p.text = mtitle
        p.font.size = Pt(10.5)
        p.font.bold = True
        p.font.color.rgb = ACCENT_YELLOW
        for l in mlines:
            pl = tf.add_paragraph()
            pl.text = "• " + l
            pl.font.size = Pt(9)
            pl.font.color.rgb = TEXT_MUTED

    add_notes(s3, "Time: 1.5 min (2:00 - 3:30)\nSpeaker Notes: This is our architectural breakdown. Notice the strict visual separation: Top is our verified deployed system in AWS eu-west-3. The request flow is API Gateway -> Lambda -> DynamoDB. API Gateway exposes the REST API with CORS enabled. Lambda validates payloads, computes running statistics, and classifies alerts based on thresholds. Events are stored in DynamoDB table CampusPulseEvents under on-demand capacity. Lambda execution permissions are managed with IAM least privilege, and execution logs stream into CloudWatch.\nCritically, at the bottom in yellow, we explicitly label proposed future enhancements that are NOT implemented: Cognito, S3/CloudFront UI, VPC isolation, and automated backups. We do not claim features that are not active.")

    # ==========================================
    # SLIDE 4: SERVERLESS IMPLEMENTATION (3:30 - 4:30)
    # ==========================================
    s4 = prs.slides.add_slide(blank_layout)
    set_slide_background(s4)
    add_header(s4, "3. Implementation & API Interface")

    # 2 Big Cards
    c1 = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.2))
    c1.fill.solid()
    c1.fill.fore_color.rgb = CARD_BG
    c1.line.color.rgb = CARD_BORDER
    tf1 = c1.text_frame
    tf1.word_wrap = True
    tf1.margin_top = Inches(0.3)
    tf1.margin_left = Inches(0.3)
    p = tf1.paragraphs[0]
    p.text = "Deployed REST Endpoints"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = ACCENT_BLUE

    endpoints = [
        ("GET /health", "Public", "Service health check (verified ok)."),
        ("POST /login", "Auth", "Demo role check (Admin/Operator), issues token."),
        ("POST /events", "Admin", "Validates & writes event record to DynamoDB."),
        ("GET /events", "Protected", "Retrieves stored events (supports ?limit=N)."),
        ("GET /stats", "Protected", "Calculates aggregated campus metrics."),
        ("GET /alerts", "Protected", "Filters events flagged as 'alert' severity.")
    ]
    for ep, badge, desc in endpoints:
        p = tf1.add_paragraph()
        p.text = f"{ep}  [{badge}]"
        p.font.size = Pt(11.5)
        p.font.bold = True
        p.font.color.rgb = ACCENT_GREEN if badge == "Public" else (ACCENT_ORANGE if badge == "Admin" else ACCENT_PURPLE)
        p.space_before = Pt(8)
        p2 = tf1.add_paragraph()
        p2.text = desc
        p2.font.size = Pt(10.5)
        p2.font.color.rgb = TEXT_LIGHT

    c2 = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.6), Inches(5.733), Inches(5.2))
    c2.fill.solid()
    c2.fill.fore_color.rgb = CARD_BG
    c2.line.color.rgb = CARD_BORDER
    tf2 = c2.text_frame
    tf2.word_wrap = True
    tf2.margin_top = Inches(0.3)
    tf2.margin_left = Inches(0.3)
    p = tf2.paragraphs[0]
    p.text = "Backend Business Logic (Python 3.12)"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = ACCENT_ORANGE

    impl_details = [
        ("Strict Schema Validation", "Rejects missing fields, invalid event types, and negative occupancy/energy values with clear 400 Bad Request messages."),
        ("Threshold Alert Engine", "Occupancy > 80 people -> 'alert'\nTemperature < 10°C or > 35°C -> 'alert'\nEnergy > 50 kWh -> 'alert'"),
        ("Campus Analytics Aggregation", "Tracks the latest reading per room (building + room key), summing active occupancy across all spaces, plus energy totals and alert counts."),
        ("Infrastructure as Code (AWS SAM)", "Declarative template.yaml defining API Gateway, Lambda function, DynamoDB table, and IAM policies.")
    ]
    for title, desc in impl_details:
        p = tf2.add_paragraph()
        p.text = title
        p.font.size = Pt(12)
        p.font.bold = True
        p.font.color.rgb = ACCENT_YELLOW
        p.space_before = Pt(10)
        p2 = tf2.add_paragraph()
        p2.text = desc
        p2.font.size = Pt(10.5)
        p2.font.color.rgb = TEXT_LIGHT

    add_notes(s4, "Time: 1 min (3:30 - 4:30)\nSpeaker Notes: Looking at implementation: Our backend is written in Python 3.12 and deployed as a single Lambda handler. We exposed 6 clean REST endpoints under the /prod stage. Ingestion via POST /events requires admin privileges, while operational reads are accessible to operators. The backend performs input sanitization, raises alerts automatically when thresholds are crossed, and aggregates telemetry dynamically without requiring separate database query daemons.")

    # ==========================================
    # SLIDE 5: SECURITY MODEL (4:30 - 5:30)
    # ==========================================
    s5 = prs.slides.add_slide(blank_layout)
    set_slide_background(s5)
    add_header(s5, "4. Security Architecture & Boundary Analysis")

    col_w = Inches(3.64)
    cards_sec = [
        ("Authentication Model", ACCENT_BLUE, [
            "Demo role authentication: Admin and Operator roles.",
            "POST /login authenticates against configured deployment credentials and issues a session Bearer token.",
            "Bearer token verification required for all non-health routes.",
            "Admin can submit events; Operator can inspect events, stats, and alerts."
        ]),
        ("Cloud Infrastructure IAM", ACCENT_GREEN, [
            "Lambda execution role follows least privilege.",
            "AWSLambdaBasicExecutionRole grants write access strictly to CloudWatch Logs.",
            "DynamoDBCrudPolicy scopes database operations exclusively to the CampusPulseEvents table ARN.",
            "No wildcard administrative permissions attached to runtime identity."
        ]),
        ("Honest Security Limits", ACCENT_ORANGE, [
            "Classroom prototype scope: Built-in credentials demonstrate concept, not enterprise identity.",
            "No production Identity Provider (IdP) like Amazon Cognito yet integrated.",
            "No custom VPC / security group network isolation; API Gateway operates on public regional endpoint.",
            "Secrets managed via SAM environment variables rather than AWS Secrets Manager."
        ])
    ]
    for i, (title, accent, bullets) in enumerate(cards_sec):
        cx = Inches(0.8) + i * (col_w + gap)
        box = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, cx, top_y, col_w, card_h)
        box.fill.solid()
        box.fill.fore_color.rgb = CARD_BG
        box.line.color.rgb = CARD_BORDER
        tf = box.text_frame
        tf.word_wrap = True
        tf.margin_top = Inches(0.3)
        tf.margin_left = Inches(0.3)
        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(16)
        p.font.bold = True
        p.font.color.rgb = accent
        for b in bullets:
            pb = tf.add_paragraph()
            pb.text = "• " + b
            pb.font.size = Pt(11.5)
            pb.font.color.rgb = TEXT_LIGHT
            pb.space_before = Pt(10)

    add_notes(s5, "Time: 1 min (4:30 - 5:30)\nSpeaker Notes: Security was an explicit consideration. On the AWS cloud side, IAM roles strictly follow least privilege: Lambda only has access to its specific DynamoDB table and its own log group. At the application layer, we implemented role differentiation between Operators and Admins using bearer tokens. We are completely transparent in noting that this demo login is educational; production readiness requires Amazon Cognito, AWS Secrets Manager, and VPC endpoints.")

    # ==========================================
    # SLIDE 6: TESTING & VALIDATION RESULTS (5:30 - 7:00)
    # ==========================================
    s6 = prs.slides.add_slide(blank_layout)
    set_slide_background(s6)
    add_header(s6, "5. Verification & Empirical Test Evidence")

    # 3 Cards
    tcard_data = [
        ("Automated Unit Tests", ACCENT_GREEN, [
            "6 automated unit tests executed via Python unittest:",
            "✓ test_valid_occupancy: Proper schema & normal severity",
            "✓ test_high_occupancy_alert: > 80 flagged as alert",
            "✓ test_missing_field_rejected: 400 Bad Request",
            "✓ test_invalid_type_rejected: Unknown types blocked",
            "✓ test_negative_occupancy_rejected: Bounds check",
            "✓ test_stats_uses_latest_occupancy_per_room",
            "Result: Ran 6 tests in 0.001s, status: OK."
        ]),
        ("Live Ingestion & Storage", ACCENT_BLUE, [
            "Ingested 4 simulated readings via generate_events.py:",
            "1. Library-A A203 (Occ: 42) -> HTTP 201 [Normal]",
            "2. Engineering Lab-02 (Energy: 18.5) -> HTTP 201 [Normal]",
            "3. Library-A A203 (Occ: 95) -> HTTP 201 [Alert]",
            "4. Engineering Lab-02 (Temp: 38°C) -> HTTP 201 [Alert]",
            "+ 1 pre-existing baseline event (Building A Room 101, Occ: 85).",
            "Verified 5 total persistent records in DynamoDB."
        ]),
        ("Analytics & 180 Occ Verified", ACCENT_PURPLE, [
            "/stats response verified against DynamoDB items:",
            "• Total events: 5",
            "• Latest occupancy returned: 180 people",
            "• Energy readings count: 1 (18.5 kWh)",
            "• Alert count: 3 (95 occ, 38°C temp, 85 occ)",
            "Occupancy 180 Math Verified:",
            "Space 1 (Library-A A203): latest = 95",
            "Space 2 (Building A Room 101): latest = 85",
            "Campus total sum across rooms: 95 + 85 = 180!"
        ])
    ]
    for i, (title, accent, bullets) in enumerate(tcard_data):
        cx = Inches(0.8) + i * (col_w + gap)
        box = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, cx, top_y, col_w, card_h)
        box.fill.solid()
        box.fill.fore_color.rgb = CARD_BG
        box.line.color.rgb = CARD_BORDER
        tf = box.text_frame
        tf.word_wrap = True
        tf.margin_top = Inches(0.25)
        tf.margin_left = Inches(0.25)
        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(15)
        p.font.bold = True
        p.font.color.rgb = accent
        for b in bullets:
            pb = tf.add_paragraph()
            pb.text = b
            pb.font.size = Pt(11)
            pb.font.color.rgb = TEXT_LIGHT if not b.startswith("✓") else ACCENT_GREEN
            pb.space_before = Pt(6)

    add_notes(s6, "Time: 1.5 min (5:30 - 7:00)\nSpeaker Notes: We thoroughly validated both local code and live deployment. All 6 unit tests passed in under 2 milliseconds. When running our event generator against the live API Gateway URL in Paris, all 4 events returned HTTP 201 and persisted into DynamoDB. An earlier question in testing was why /stats reported 180 people occupancy. We traced this mathematically to the backend aggregation logic: The system sums the most recent reading for each distinct monitored room. Room A203 had 95 people, Room 101 had 85 people. 95 plus 85 equals 180. The math is completely accurate.")

    # ==========================================
    # SLIDE 7: COST & SCALABILITY (7:00 - 8:00)
    # ==========================================
    s7 = prs.slides.add_slide(blank_layout)
    set_slide_background(s7)
    add_header(s7, "6. Cloud Cost Analysis & Scalability Governance")

    c1 = s7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.2))
    c1.fill.solid()
    c1.fill.fore_color.rgb = CARD_BG
    c1.line.color.rgb = CARD_BORDER
    tf1 = c1.text_frame
    tf1.word_wrap = True
    tf1.margin_top = Inches(0.3)
    tf1.margin_left = Inches(0.3)
    p = tf1.paragraphs[0]
    p.text = "Cost Optimization & Free Tier Breakdown"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = ACCENT_YELLOW

    cost_items = [
        ("Amazon API Gateway (REST)", "$3.50 per million calls. For demonstration & testing (~100 calls): $0.00035."),
        ("AWS Lambda (Serverless Compute)", "Free Tier includes 1M requests & 3.2M sec compute/month. Our 256MB execution (~50ms duration) incurred $0.00."),
        ("Amazon DynamoDB (On-Demand)", "Free Tier provides 25GB storage. Pay-per-request is $1.25/million writes. Prototype storage & reads incurred $0.00."),
        ("Amazon CloudWatch Logs", "Free Tier includes 5GB log ingestion/month. Total logging volume was under 5 MB ($0.00)."),
        ("Active Cost Control", "Configured AWS Budget Alert to prevent billing surprises; zero running EC2/NAT instance idle charges.")
    ]
    for title, desc in cost_items:
        p = tf1.add_paragraph()
        p.text = title
        p.font.size = Pt(11.5)
        p.font.bold = True
        p.font.color.rgb = ACCENT_GREEN
        p.space_before = Pt(8)
        p2 = tf1.add_paragraph()
        p2.text = desc
        p2.font.size = Pt(10.5)
        p2.font.color.rgb = TEXT_LIGHT

    c2 = s7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.6), Inches(5.733), Inches(5.2))
    c2.fill.solid()
    c2.fill.fore_color.rgb = CARD_BG
    c2.line.color.rgb = CARD_BORDER
    tf2 = c2.text_frame
    tf2.word_wrap = True
    tf2.margin_top = Inches(0.3)
    tf2.margin_left = Inches(0.3)
    p = tf2.paragraphs[0]
    p.text = "Scalability Dynamics & Scaling Limits"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = ACCENT_BLUE

    scale_items = [
        ("Serverless Auto-Scaling", "Lambda automatically provisions concurrent execution environments based on incoming HTTP request volume up to regional account concurrency."),
        ("DynamoDB On-Demand Mode", "PAY_PER_REQUEST billing accommodates unpredictable bursty sensor traffic without manual capacity planning or throttling."),
        ("Current Bottleneck: Table Scan", "Backend currently uses table.scan() to aggregate statistics. While completely fine for <1,000 demo events, high production volumes would cause latency and cost spikes."),
        ("Scaling Path to Production", "Implement DynamoDB Global Secondary Indexes (GSIs) by room and timestamp, DynamoDB Streams for real-time aggregation, and client-side pagination.")
    ]
    for title, desc in scale_items:
        p = tf2.add_paragraph()
        p.text = title
        p.font.size = Pt(11.5)
        p.font.bold = True
        p.font.color.rgb = ACCENT_ORANGE
        p.space_before = Pt(8)
        p2 = tf2.add_paragraph()
        p2.text = desc
        p2.font.size = Pt(10.5)
        p2.font.color.rgb = TEXT_LIGHT

    add_notes(s7, "Time: 1 min (7:00 - 8:00)\nSpeaker Notes: By choosing AWS serverless technologies, we minimized costs: No idle server fees, no active NAT Gateways. Total testing cost was under 1 cent and well within the AWS Free Tier. In terms of scalability, Lambda and DynamoDB scale automatically with incoming traffic. However, we critically acknowledge an architectural limit: our aggregation currently relies on DynamoDB scans, which works for a demo dataset but would require GSIs and DynamoDB Streams at university-wide scale.")

    # ==========================================
    # SLIDE 8: FUTURE ENHANCEMENTS (8:00 - 9:00)
    # ==========================================
    s8 = prs.slides.add_slide(blank_layout)
    set_slide_background(s8)
    add_header(s8, "7. Production Roadmap — Proposed Future Enhancements", "Clearly Distinguished from Current Implemented Deliverables")

    grid_items = [
        ("1. Production Identity (Amazon Cognito)", ACCENT_BLUE, [
            "Cognito User Pools with JWT verification.",
            "API Gateway HTTP Authorizer validating token claims.",
            "Multi-Factor Authentication (MFA) & self-service password recovery.",
            "Fine-grained RBAC with IAM group scoping."
        ]),
        ("2. Interactive Web Dashboard & CDN", ACCENT_PURPLE, [
            "React / Next.js web portal for operators.",
            "Static hosting on Amazon S3 with Amazon CloudFront CDN edge caching.",
            "Real-time sensor graphs, live floor plans, and interactive threshold configuration.",
            "API Gateway WebSockets for instant push updates."
        ]),
        ("3. Network Isolation & Secret Security", ACCENT_ORANGE, [
            "Enclose Lambda in Amazon VPC private subnets.",
            "VPC Gateway Endpoints to route DynamoDB traffic privately without public internet traversal.",
            "AWS Secrets Manager for automatic credential rotation.",
            "AWS WAF attached to API Gateway for DDoS & injection defense."
        ]),
        ("4. Automated Disaster Recovery & Push Alerts", ACCENT_GREEN, [
            "Enable DynamoDB Point-in-Time Recovery (PITR) with continuous backups.",
            "Scheduled AWS Backup plans with cross-region replication for RPO < 15 min.",
            "Amazon CloudWatch Metric Alarms triggering Amazon SNS.",
            "Instant SMS and email notifications to maintenance crews."
        ])
    ]

    gx_offsets = [Inches(0.8), Inches(6.8), Inches(0.8), Inches(6.8)]
    gy_offsets = [Inches(1.6), Inches(1.6), Inches(4.3), Inches(4.3)]

    for i, (mtitle, col, mbullets) in enumerate(grid_items):
        box = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, gx_offsets[i], gy_offsets[i], Inches(5.733), Inches(2.5))
        box.fill.solid()
        box.fill.fore_color.rgb = FUTURE_BG
        box.line.color.rgb = FUTURE_BORDER
        box.line.width = Pt(1.5)
        tf = box.text_frame
        tf.word_wrap = True
        tf.margin_top = Inches(0.18)
        tf.margin_left = Inches(0.25)
        p = tf.paragraphs[0]
        p.text = mtitle
        p.font.size = Pt(13)
        p.font.bold = True
        p.font.color.rgb = ACCENT_YELLOW
        for b in mbullets:
            pb = tf.add_paragraph()
            pb.text = "• " + b
            pb.font.size = Pt(10)
            pb.font.color.rgb = TEXT_LIGHT
            pb.space_before = Pt(3)

    add_notes(s8, "Time: 1 min (8:00 - 9:00)\nSpeaker Notes: To be completely transparent about our engineering boundaries, we compiled a clear production roadmap. None of these items are claimed as implemented today. For production, the priority steps would be: First, replacing demo credentials with Cognito. Second, adding an S3/CloudFront web portal. Third, enclosing compute within a VPC with Gateway endpoints. And fourth, enabling DynamoDB Point-in-Time Recovery and SNS push alerts.")

    # ==========================================
    # SLIDE 9: CONCLUSION & DEMO PLAN (9:00 - 10:00)
    # ==========================================
    s9 = prs.slides.add_slide(blank_layout)
    set_slide_background(s9)
    add_header(s9, "8. Conclusion & Live Demonstration Plan")

    c1 = s9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.2))
    c1.fill.solid()
    c1.fill.fore_color.rgb = CARD_BG
    c1.line.color.rgb = CARD_BORDER
    tf1 = c1.text_frame
    tf1.word_wrap = True
    tf1.margin_top = Inches(0.3)
    tf1.margin_left = Inches(0.3)
    p = tf1.paragraphs[0]
    p.text = "Project Summary & Key Takeaways"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = ACCENT_GREEN

    concl_points = [
        ("Delivered Serverless Architecture", "Successfully deployed a working cloud monitoring pipeline on AWS eu-west-3 using SAM, API Gateway, Lambda, and DynamoDB."),
        ("Empirical Reliability", "Passed 6 unit tests; validated end-to-end data flow with 4 live ingested events; confirmed threshold alerting and cross-room aggregation."),
        ("Architectural Honesty", "Documented exact operational boundaries; avoided inflating claims; clearly separated live components from future proposed additions."),
        ("Cost & Operational Discipline", "Operated strictly within Free Tier parameters; monitored CloudWatch logs; established budget safety.")
    ]
    for title, desc in concl_points:
        p = tf1.add_paragraph()
        p.text = title
        p.font.size = Pt(11.5)
        p.font.bold = True
        p.font.color.rgb = ACCENT_BLUE
        p.space_before = Pt(8)
        p2 = tf1.add_paragraph()
        p2.text = desc
        p2.font.size = Pt(10.5)
        p2.font.color.rgb = TEXT_LIGHT

    c2 = s9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.6), Inches(5.733), Inches(5.2))
    c2.fill.solid()
    c2.fill.fore_color.rgb = CARD_BG
    c2.line.color.rgb = CARD_BORDER
    tf2 = c2.text_frame
    tf2.word_wrap = True
    tf2.margin_top = Inches(0.3)
    tf2.margin_left = Inches(0.3)
    p = tf2.paragraphs[0]
    p.text = "10-Minute Live Demo Sequence"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = ACCENT_ORANGE

    demo_steps = [
        ("Step 1: Health Check (15s)", "GET /health -> Verified HTTP 200 {'status': 'ok', 'service': 'CampusPulse 2026'}."),
        ("Step 2: Authentication & Token (20s)", "POST /login -> Returns bearer token for Operator/Admin."),
        ("Step 3: Stored Events Inspection (25s)", "GET /events -> Displays 5 live records across Library-A, Engineering, and Building A."),
        ("Step 4: Real-Time Stats (25s)", "GET /stats -> Displays aggregated count: 5 events, 180 occupancy, 18.5 kWh energy, 3 alerts."),
        ("Step 5: Alert Trigger Verification (25s)", "GET /alerts -> Displays the 3 abnormal readings (occupancy 95 & 85, temp 38°C)."),
        ("Step 6: Observability (15s)", "CloudWatch Logs -> Show real-time Lambda execution stream.")
    ]
    for step, desc in demo_steps:
        p = tf2.add_paragraph()
        p.text = step
        p.font.size = Pt(11.5)
        p.font.bold = True
        p.font.color.rgb = ACCENT_YELLOW
        p.space_before = Pt(6)
        p2 = tf2.add_paragraph()
        p2.text = desc
        p2.font.size = Pt(10)
        p2.font.color.rgb = TEXT_LIGHT

    add_notes(s9, "Time: 1 min (9:00 - 10:00)\nSpeaker Notes: To conclude, CampusPulse 2026 demonstrates how modern serverless services on AWS can be architected to solve practical campus operations challenges in an event-driven, cost-effective, and observable manner. We are now happy to show our live demo sequence following steps 1 through 6, and answer any questions from the panel. Thank you!")

    out_pptx = Path("submission/CampusPulse2026_Presentation.pptx")
    prs.save(str(out_pptx))
    print(f"PowerPoint Presentation created: {out_pptx.resolve()} ({out_pptx.stat().st_size} bytes)")

if __name__ == "__main__":
    build_presentation()
