"""
Generate a professional SVG architecture diagram for CampusPulse 2026.
Accurately shows ONLY deployed components in the main section,
and puts future enhancements in a clearly separated section:
"Proposed Future Enhancements — Not Implemented".
"""
from pathlib import Path

svg_content = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 820" width="1200" height="820" style="background:#0f172a; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
  <defs>
    <!-- Gradients -->
    <linearGradient id="headerGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#3b82f6" />
      <stop offset="100%" stop-color="#8b5cf6" />
    </linearGradient>
    <linearGradient id="deployedBoxGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1e293b" />
      <stop offset="100%" stop-color="#0f172a" />
    </linearGradient>
    <linearGradient id="futureBoxGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1e293b" />
      <stop offset="100%" stop-color="#18181b" />
    </linearGradient>
    
    <!-- Component Gradients -->
    <linearGradient id="apiGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284c7" />
      <stop offset="100%" stop-color="#0369a1" />
    </linearGradient>
    <linearGradient id="lambdaGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ea580c" />
      <stop offset="100%" stop-color="#c2410c" />
    </linearGradient>
    <linearGradient id="ddbGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#2563eb" />
      <stop offset="100%" stop-color="#1d4ed8" />
    </linearGradient>
    <linearGradient id="cwGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ec4899" />
      <stop offset="100%" stop-color="#be185d" />
    </linearGradient>
    <linearGradient id="iamGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#dc2626" />
      <stop offset="100%" stop-color="#991b1b" />
    </linearGradient>

    <!-- Filters for subtle drop shadows -->
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000000" flood-opacity="0.4" />
    </filter>
    <filter id="glow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="0" stdDeviation="4" flood-color="#38bdf8" flood-opacity="0.3"/>
    </filter>
    
    <!-- Arrow marker -->
    <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#38bdf8" />
    </marker>
    <marker id="arrowOrange" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#f97316" />
    </marker>
    <marker id="arrowDashed" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#94a3b8" />
    </marker>
  </defs>

  <!-- Title & Top Banner -->
  <rect x="0" y="0" width="1200" height="70" fill="#0b1120" />
  <rect x="0" y="68" width="1200" height="2" fill="url(#headerGrad)" />
  <text x="40" y="42" fill="#f8fafc" font-size="22" font-weight="700" letter-spacing="0.5">CampusPulse 2026 — Cloud System Architecture</text>
  <text x="820" y="42" fill="#94a3b8" font-size="13" font-weight="500">Region: AWS eu-west-3 (Paris) | SAM Deployed</text>

  <!-- ========================================== -->
  <!-- SECTION 1: ACTUALLY DEPLOYED ARCHITECTURE -->
  <!-- ========================================== -->
  <rect x="30" y="90" width="1140" height="490" rx="12" fill="url(#deployedBoxGrad)" stroke="#334155" stroke-width="1.5" filter="url(#shadow)" />
  
  <!-- Section Badge -->
  <rect x="45" y="105" width="280" height="28" rx="6" fill="#166534" />
  <circle cx="60" cy="119" r="5" fill="#4ade80" />
  <text x="75" y="124" fill="#f0fdf4" font-size="12" font-weight="700" letter-spacing="0.5">VERIFIED LIVE ARCHITECTURE (DEPLOYED)</text>

  <!-- 1. Client / Data Source Layer -->
  <g transform="translate(60, 160)">
    <rect x="0" y="0" width="180" height="270" rx="10" fill="#1e293b" stroke="#475569" stroke-width="1.5" />
    <rect x="0" y="0" width="180" height="36" rx="10" fill="#334155" />
    <text x="15" y="24" fill="#e2e8f0" font-size="13" font-weight="600">Client / Ingestion Layer</text>
    
    <!-- Python Event Generator Box -->
    <rect x="15" y="55" width="150" height="85" rx="6" fill="#0f172a" stroke="#64748b" stroke-width="1" />
    <text x="25" y="77" fill="#38bdf8" font-size="12" font-weight="700">Event Generator</text>
    <text x="25" y="95" fill="#94a3b8" font-size="10">generate_events.py</text>
    <text x="25" y="112" fill="#cbd5e1" font-size="10">Simulated Telemetry</text>
    <text x="25" y="126" fill="#64748b" font-size="9">(Occupancy, Energy, Temp)</text>

    <!-- REST Client / Admin Box -->
    <rect x="15" y="155" width="150" height="85" rx="6" fill="#0f172a" stroke="#64748b" stroke-width="1" />
    <text x="25" y="177" fill="#a78bfa" font-size="12" font-weight="700">Operations Client</text>
    <text x="25" y="195" fill="#94a3b8" font-size="10">PowerShell / Curl / Browser</text>
    <text x="25" y="212" fill="#cbd5e1" font-size="10">Roles: Admin &amp; Operator</text>
    <text x="25" y="226" fill="#64748b" font-size="9">Bearer Token Auth</text>
  </g>

  <!-- Connection: Client -> API Gateway -->
  <path d="M 240 240 L 320 240" fill="none" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#arrow)" />
  <rect x="250" y="215" width="60" height="18" rx="4" fill="#0f172a" stroke="#38bdf8" stroke-width="1" />
  <text x="257" y="228" fill="#38bdf8" font-size="9" font-weight="600">HTTPS / TLS</text>

  <!-- 2. Amazon API Gateway -->
  <g transform="translate(325, 160)">
    <rect x="0" y="0" width="220" height="270" rx="10" fill="#1e293b" stroke="#0284c7" stroke-width="1.5" />
    <rect x="0" y="0" width="220" height="36" rx="10" fill="url(#apiGrad)" />
    <text x="15" y="24" fill="#ffffff" font-size="13" font-weight="700">Amazon API Gateway</text>
    <text x="15" y="52" fill="#38bdf8" font-size="11" font-weight="600">REST API (Stage: prod)</text>
    <text x="15" y="67" fill="#64748b" font-size="9">Endpoint: Regional (eu-west-3)</text>

    <!-- Endpoints List -->
    <rect x="12" y="78" width="196" height="175" rx="6" fill="#0f172a" stroke="#334155" stroke-width="1" />
    
    <text x="22" y="98" fill="#4ade80" font-size="10" font-weight="700">GET</text>
    <text x="52" y="98" fill="#e2e8f0" font-size="10">/health</text>
    <text x="150" y="98" fill="#94a3b8" font-size="9">(Public)</text>

    <text x="22" y="123" fill="#f59e0b" font-size="10" font-weight="700">POST</text>
    <text x="56" y="123" fill="#e2e8f0" font-size="10">/login</text>
    <text x="135" y="123" fill="#94a3b8" font-size="9">(Auth check)</text>

    <text x="22" y="148" fill="#f59e0b" font-size="10" font-weight="700">POST</text>
    <text x="56" y="148" fill="#e2e8f0" font-size="10">/events</text>
    <text x="135" y="148" fill="#f43f5e" font-size="9">[Admin only]</text>

    <text x="22" y="173" fill="#4ade80" font-size="10" font-weight="700">GET</text>
    <text x="52" y="173" fill="#e2e8f0" font-size="10">/events</text>
    <text x="135" y="173" fill="#94a3b8" font-size="9">[Protected]</text>

    <text x="22" y="198" fill="#4ade80" font-size="10" font-weight="700">GET</text>
    <text x="52" y="198" fill="#e2e8f0" font-size="10">/stats</text>
    <text x="135" y="198" fill="#94a3b8" font-size="9">[Protected]</text>

    <text x="22" y="223" fill="#4ade80" font-size="10" font-weight="700">GET</text>
    <text x="52" y="223" fill="#e2e8f0" font-size="10">/alerts</text>
    <text x="135" y="223" fill="#94a3b8" font-size="9">[Protected]</text>

    <text x="22" y="243" fill="#64748b" font-size="9">CORS enabled: *</text>
  </g>

  <!-- Connection: API Gateway -> Lambda -->
  <path d="M 545 280 L 615 280" fill="none" stroke="#f97316" stroke-width="2.5" marker-end="url(#arrowOrange)" />
  <rect x="552" y="258" width="55" height="18" rx="4" fill="#0f172a" stroke="#f97316" stroke-width="1" />
  <text x="557" y="271" fill="#f97316" font-size="9" font-weight="600">Proxy Inv</text>

  <!-- 3. AWS Lambda Function -->
  <g transform="translate(620, 160)">
    <rect x="0" y="0" width="250" height="270" rx="10" fill="#1e293b" stroke="#ea580c" stroke-width="1.5" />
    <rect x="0" y="0" width="250" height="36" rx="10" fill="url(#lambdaGrad)" />
    <text x="15" y="24" fill="#ffffff" font-size="13" font-weight="700">AWS Lambda (CampusPulseFunction)</text>
    <text x="15" y="52" fill="#fb923c" font-size="11" font-weight="600">Runtime: Python 3.12 | 256 MB</text>
    <text x="15" y="67" fill="#64748b" font-size="9">Timeout: 15s | Handler: main.lambda_handler</text>

    <!-- Function Internal Logic -->
    <rect x="12" y="78" width="226" height="175" rx="6" fill="#0f172a" stroke="#334155" stroke-width="1" />
    <text x="22" y="98" fill="#e2e8f0" font-size="11" font-weight="600">Embedded Application Logic:</text>
    
    <circle cx="27" cy="118" r="3" fill="#38bdf8" />
    <text x="36" y="122" fill="#cbd5e1" font-size="10">Event Validation (_normalise_event)</text>
    
    <circle cx="27" cy="143" r="3" fill="#f43f5e" />
    <text x="36" y="147" fill="#cbd5e1" font-size="10">Threshold Classification:</text>
    <text x="40" y="162" fill="#94a3b8" font-size="9">Occ &gt; 80, Temp &lt; 10/&gt; 35, Energy &gt; 50</text>

    <circle cx="27" cy="183" r="3" fill="#a855f7" />
    <text x="36" y="187" fill="#cbd5e1" font-size="10">Operations Analytics (_stats):</text>
    <text x="40" y="202" fill="#94a3b8" font-size="9">Sums latest occupancy across rooms</text>

    <circle cx="27" cy="223" r="3" fill="#fbbf24" />
    <text x="36" y="227" fill="#cbd5e1" font-size="10">Role Auth: Admin / Operator</text>
  </g>

  <!-- Connection: Lambda -> DynamoDB -->
  <path d="M 870 280 L 940 280" fill="none" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#arrow)" />
  <rect x="878" y="258" width="55" height="18" rx="4" fill="#0f172a" stroke="#38bdf8" stroke-width="1" />
  <text x="882" y="271" fill="#38bdf8" font-size="9" font-weight="600">CRUD / Scan</text>

  <!-- 4. Amazon DynamoDB -->
  <g transform="translate(945, 160)">
    <rect x="0" y="0" width="200" height="270" rx="10" fill="#1e293b" stroke="#2563eb" stroke-width="1.5" />
    <rect x="0" y="0" width="200" height="36" rx="10" fill="url(#ddbGrad)" />
    <text x="15" y="24" fill="#ffffff" font-size="13" font-weight="700">Amazon DynamoDB</text>
    <text x="15" y="52" fill="#60a5fa" font-size="11" font-weight="600">Table: CampusPulseEvents</text>
    <text x="15" y="67" fill="#64748b" font-size="9">Billing: PAY_PER_REQUEST</text>

    <!-- DynamoDB Details -->
    <rect x="12" y="78" width="176" height="175" rx="6" fill="#0f172a" stroke="#334155" stroke-width="1" />
    <text x="22" y="100" fill="#e2e8f0" font-size="11" font-weight="600">Key Schema:</text>
    <text x="22" y="118" fill="#38bdf8" font-size="10">Partition Key: event_id (S)</text>

    <text x="22" y="145" fill="#e2e8f0" font-size="11" font-weight="600">Attributes Stored:</text>
    <text x="22" y="163" fill="#cbd5e1" font-size="10">• building, room</text>
    <text x="22" y="180" fill="#cbd5e1" font-size="10">• event_type, value, unit</text>
    <text x="22" y="197" fill="#cbd5e1" font-size="10">• severity (normal / alert)</text>
    <text x="22" y="214" fill="#cbd5e1" font-size="10">• timestamp (ISO 8601)</text>
    
    <text x="22" y="241" fill="#64748b" font-size="9">Access: PutItem &amp; Scan</text>
  </g>

  <!-- Cross-Cutting Support: IAM & CloudWatch -->
  <!-- IAM Permissions Block -->
  <g transform="translate(420, 460)">
    <rect x="0" y="0" width="250" height="95" rx="8" fill="#1e293b" stroke="#dc2626" stroke-width="1.2" />
    <rect x="0" y="0" width="250" height="26" rx="8" fill="url(#iamGrad)" />
    <text x="12" y="18" fill="#ffffff" font-size="11" font-weight="700">AWS IAM (Execution Role)</text>
    <text x="12" y="44" fill="#fca5a5" font-size="10" font-weight="600">Least-Privilege Policies:</text>
    <text x="12" y="60" fill="#cbd5e1" font-size="9">• AWSLambdaBasicExecutionRole (Logs)</text>
    <text x="12" y="75" fill="#cbd5e1" font-size="9">• DynamoDBCrudPolicy (CampusPulseEvents)</text>
    <text x="12" y="88" fill="#94a3b8" font-size="8">Managed via CloudFormation template.yaml</text>
  </g>

  <!-- Connection: IAM -> Lambda -->
  <path d="M 545 460 L 650 430" fill="none" stroke="#dc2626" stroke-width="1.5" stroke-dasharray="4,3" marker-end="url(#arrowDashed)" />

  <!-- CloudWatch Logs Block -->
  <g transform="translate(710, 460)">
    <rect x="0" y="0" width="280" height="95" rx="8" fill="#1e293b" stroke="#ec4899" stroke-width="1.2" />
    <rect x="0" y="0" width="280" height="26" rx="8" fill="url(#cwGrad)" />
    <text x="12" y="18" fill="#ffffff" font-size="11" font-weight="700">Amazon CloudWatch Logs</text>
    <text x="12" y="44" fill="#f472b6" font-size="10" font-weight="600">Log Group:</text>
    <text x="12" y="59" fill="#e2e8f0" font-size="9">/aws/lambda/campuspulse-2026-...</text>
    <text x="12" y="74" fill="#cbd5e1" font-size="9">• Verified 1 live log stream ($LATEST)</text>
    <text x="12" y="88" fill="#94a3b8" font-size="8">Captures invocations, errors, and runtimes</text>
  </g>

  <!-- Connection: Lambda -> CloudWatch -->
  <path d="M 750 430 L 780 460" fill="none" stroke="#ec4899" stroke-width="1.5" stroke-dasharray="4,3" marker-end="url(#arrowDashed)" />


  <!-- ========================================================== -->
  <!-- SECTION 2: PROPOSED FUTURE ENHANCEMENTS — NOT IMPLEMENTED  -->
  <!-- ========================================================== -->
  <rect x="30" y="600" width="1140" height="195" rx="12" fill="url(#futureBoxGrad)" stroke="#eab308" stroke-width="1.5" stroke-dasharray="6,4" />
  
  <!-- Section Badge -->
  <rect x="45" y="612" width="410" height="26" rx="6" fill="#854d0e" />
  <circle cx="60" cy="625" r="5" fill="#fde047" />
  <text x="75" y="630" fill="#fef9c3" font-size="12" font-weight="700" letter-spacing="0.5">PROPOSED FUTURE ENHANCEMENTS — NOT IMPLEMENTED</text>
  <text x="470" y="630" fill="#fbbf24" font-size="11" font-style="italic">Clearly isolated from current deployment scope</text>

  <!-- 4 Future Enhancement Modules -->
  <!-- 1. Amazon Cognito -->
  <g transform="translate(50, 650)">
    <rect x="0" y="0" width="250" height="130" rx="8" fill="#0f172a" stroke="#ca8a04" stroke-width="1" />
    <rect x="0" y="0" width="250" height="24" rx="8" fill="#292524" />
    <text x="10" y="17" fill="#fef08a" font-size="11" font-weight="700">1. Production Identity (Cognito)</text>
    <text x="10" y="42" fill="#cbd5e1" font-size="10">• Amazon Cognito User Pools</text>
    <text x="10" y="58" fill="#94a3b8" font-size="9">• OAuth2 / JWT Authorizer in API Gateway</text>
    <text x="10" y="74" fill="#94a3b8" font-size="9">• Role-based fine-grained scopes</text>
    <text x="10" y="90" fill="#94a3b8" font-size="9">• MFA &amp; self-service password reset</text>
    <text x="10" y="112" fill="#f87171" font-size="9" font-weight="600">[Status: Not Implemented]</text>
  </g>

  <!-- 2. Web Dashboard & CDN -->
  <g transform="translate(325, 650)">
    <rect x="0" y="0" width="250" height="130" rx="8" fill="#0f172a" stroke="#ca8a04" stroke-width="1" />
    <rect x="0" y="0" width="250" height="24" rx="8" fill="#292524" />
    <text x="10" y="17" fill="#fef08a" font-size="11" font-weight="700">2. UI Dashboard &amp; CloudFront</text>
    <text x="10" y="42" fill="#cbd5e1" font-size="10">• Single Page App (React / Next.js)</text>
    <text x="10" y="58" fill="#94a3b8" font-size="9">• Static hosting via Amazon S3 bucket</text>
    <text x="10" y="74" fill="#94a3b8" font-size="9">• Amazon CloudFront CDN distribution</text>
    <text x="10" y="90" fill="#94a3b8" font-size="9">• Real-time WebSocket subscriptions</text>
    <text x="10" y="112" fill="#f87171" font-size="9" font-weight="600">[Status: Not Implemented]</text>
  </g>

  <!-- 3. Network Isolation & Secrets -->
  <g transform="translate(600, 650)">
    <rect x="0" y="0" width="250" height="130" rx="8" fill="#0f172a" stroke="#ca8a04" stroke-width="1" />
    <rect x="0" y="0" width="250" height="24" rx="8" fill="#292524" />
    <text x="10" y="17" fill="#fef08a" font-size="11" font-weight="700">3. Network VPC &amp; Secrets</text>
    <text x="10" y="42" fill="#cbd5e1" font-size="10">• Custom Amazon VPC (Private Subnets)</text>
    <text x="10" y="58" fill="#94a3b8" font-size="9">• DynamoDB VPC Gateway Endpoint</text>
    <text x="10" y="74" fill="#94a3b8" font-size="9">• AWS Secrets Manager credential store</text>
    <text x="10" y="90" fill="#94a3b8" font-size="9">• AWS WAF rate limiting &amp; firewall</text>
    <text x="10" y="112" fill="#f87171" font-size="9" font-weight="600">[Status: Not Implemented]</text>
  </g>

  <!-- 4. Resilience, Alarms & Streaming -->
  <g transform="translate(875, 650)">
    <rect x="0" y="0" width="280" height="130" rx="8" fill="#0f172a" stroke="#ca8a04" stroke-width="1" />
    <rect x="0" y="0" width="280" height="24" rx="8" fill="#292524" />
    <text x="10" y="17" fill="#fef08a" font-size="11" font-weight="700">4. Automated DR &amp; Push Alerts</text>
    <text x="10" y="42" fill="#cbd5e1" font-size="10">• DynamoDB Point-in-Time Recovery (PITR)</text>
    <text x="10" y="58" fill="#94a3b8" font-size="9">• AWS Backup scheduled daily plans</text>
    <text x="10" y="74" fill="#94a3b8" font-size="9">• CloudWatch Metric Alarms &amp; SNS email/SMS</text>
    <text x="10" y="90" fill="#94a3b8" font-size="9">• Amazon SQS / Kinesis stream ingestion</text>
    <text x="10" y="112" fill="#f87171" font-size="9" font-weight="600">[Status: Not Implemented]</text>
  </g>

</svg>"""

out_svg = Path("submission/architecture_diagram.svg")
out_svg.write_text(svg_content.strip(), encoding="utf-8")
print(f"Generated {out_svg.resolve()} ({out_svg.stat().st_size} bytes)")
