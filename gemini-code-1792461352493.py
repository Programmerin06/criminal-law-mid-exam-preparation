import os
from weasyprint import HTML

# Create the 5-part (A~E) Essay Blank Test Sheet PDF matching the requested layout
html_content = """
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>75분 시험 대비 서술식 답안 훈련 백지 테스트지 (A~E)</title>
    <style>
        @page {
            size: A4 portrait;
            margin: 0;
        }
        *, *::before, *::after {
            box-sizing: border-box;
        }
        body {
            font-family: 'Malgun Gothic', 'Apple SD Gothic Neo', sans-serif;
            margin: 0;
            padding: 0;
            background-color: #ffffff;
            color: #222222;
            -webkit-print-color-adjust: exact;
        }

        .page {
            width: 210mm;
            height: 297mm;
            position: relative;
            page-break-after: always;
            box-sizing: border-box;
            background-color: #ffffff;
            display: flex;
            flex-direction: column;
        }

        /* Top and Bottom Wood/Tan Banner Lines matching image style */
        .top-bar {
            height: 14px;
            background-color: #e0be9b;
            border-bottom: 2px solid #c8a37f;
            width: 100%;
        }
        .bottom-bar {
            height: 14px;
            background-color: #e0be9b;
            border-top: 2px solid #c8a37f;
            width: 100%;
            position: absolute;
            bottom: 0;
            left: 0;
        }

        /* Header Info Area */
        .header-area {
            padding: 10px 18px 6px 18px;
            background-color: #fbf9f5;
            border-bottom: 1.5px solid #d8cdb0;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .header-title {
            font-size: 11pt;
            font-weight: bold;
            color: #4a3828;
            display: flex;
            align-items: center;
            gap: 6px;
        }
        .header-title span.badge {
            background-color: #7a5030;
            color: white;
            padding: 2px 7px;
            border-radius: 3px;
            font-size: 9.5pt;
        }
        .header-timer {
            font-size: 8.5pt;
            color: #765941;
            font-weight: bold;
            background-color: #eee4d4;
            padding: 3px 8px;
            border-radius: 4px;
            border: 1px solid #d4c2aa;
        }

        /* Main Split Container (Left / Right) */
        .content-container {
            flex: 1;
            display: flex;
            position: relative;
            margin-bottom: 14px; /* clearance for bottom bar */
        }

        /* Center Vertical Divider Line matching image */
        .center-line {
            position: absolute;
            left: 50%;
            top: 0;
            bottom: 0;
            width: 1.5px;
            background-color: #b0a490;
            z-index: 10;
        }

        /* Column Styles */
        .column {
            width: 50%;
            padding: 8px 12px;
            box-sizing: border-box;
            display: flex;
            flex-direction: column;
        }
        .column-left {
            padding-right: 14px;
            background-color: #ffffff;
        }
        .column-right {
            padding-left: 14px;
            background-color: #fcfbfa;
        }

        /* Column Section Titles */
        .col-title {
            font-size: 9.5pt;
            font-weight: bold;
            padding: 4px 8px;
            margin-bottom: 6px;
            border-radius: 3px;
            text-align: center;
        }
        .col-title-left {
            background-color: #e8ded1;
            color: #3b2a1a;
            border: 1px solid #cbbba8;
        }
        .col-title-right {
            background-color: #2b3a4a;
            color: #ffffff;
            border: 1px solid #1a2634;
        }

        /* Lined Note Paper Effect */
        .ruled-lines {
            flex: 1;
            background-image: linear-gradient(to bottom, transparent 23px, #e2dacd 24px);
            background-size: 100% 24px;
            line-height: 24px;
            font-size: 8.8pt;
            color: #1e293b;
            padding-top: 1px;
        }

        /* Formatting inside Model Answer Column */
        .model-answer p {
            margin: 0;
            line-height: 24px;
        }
        .model-answer h4 {
            margin: 0;
            line-height: 24px;
            font-size: 9pt;
            color: #1b365d;
            font-weight: bold;
        }
        .model-answer .sec-title {
            color: #8b0000;
            font-weight: bold;
        }
        .model-answer ul, .model-answer ol {
            margin: 0;
            padding-left: 16px;
        }
        .model-answer li {
            line-height: 24px;
        }

        /* Time allocation guidance box inside Left Column */
        .time-guide {
            font-size: 8pt;
            line-height: 18px;
            color: #5c4328;
            background-color: #f7f1e5;
            border: 1px dashed #c0ad94;
            padding: 4px 8px;
            border-radius: 4px;
            margin-bottom: 6px;
        }
        .time-guide strong {
            color: #8c3b00;
        }
    </style>
</head>
<body>

<!-- PAGE A -->
<div class="page">
    <div class="top-bar"></div>
    <div class="header-area">
        <div class="header-title">
            <span class="badge">주제 A</span> 죄형법정주의와 법률주의 (명령 vs 조례)
        </div>
        <div class="header-timer">⏱️ 목표시간: 10분 [서론 2분 | 본론 6분 | 결론 2분]</div>
    </div>
    
    <div class="content-container">
        <div class="center-line"></div>
        
        <!-- LEFT: Blank Writing Area -->
        <div class="column column-left">
            <div class="col-title col-title-left">✍️ 나의 답안 작성란 (서-본-결 시간 안배 훈련)</div>
            <div class="time-guide">
                <strong>💡 [시간 안배 가이드]</strong><br>
                • <strong>서론 (0~2분)</strong>: 조례의 형벌 부과 가능성 및 민주주의 원리 제기<br>
                • <strong>본론 (2~8분)</strong>: 명령과 조례의 위임 비교 (표 구분) 및 위헌성 판단 법리<br>
                • <strong>결론 (8~10분)</strong>: 사안 조례의 위헌 여부 최종 소결
            </div>
            <div class="ruled-lines">
                <!-- Blank lines for student writing -->
            </div>
        </div>
        
        <!-- RIGHT: Model Answer -->
        <div class="column column-right">
            <div class="col-title col-title-right">🎓 교수님 스타일 A+ 모범 답안</div>
            <div class="ruled-lines model-answer">
                <h4>Ⅰ. 문제의 제기 (서론)</h4>
                <p>죄형법정주의의 법률주의상 형벌은 국회가 제정한 법률로 정함이 원칙이다. 다만 조례로 주민의 권리제한 및 형벌을 부과할 때 위임의 정도와 위헌 여부가 문제된다.</p>
                <h4>Ⅱ. 명령과 조례의 위임법리 비교 (본론)</h4>
                <p>1. <strong>행정입법(명령)의 법률주의:</strong> 포괄적 위임이 금지되며, 구체적으로 범위를 정한 명시적 위임이 있는 경우에만 예외적으로 허용된다.</p>
                <p>2. <strong>조례의 법률주의:</strong> 지방자치단체는 자치입법권을 가지므로, 주민의 권리 제한·의무 부과에 법률의 위임이 필요하지만, 명령과 달리 <u>포괄적 위임도 허용</u>된다.</p>
                <p>3. <strong>판례의 태도:</strong> 조례에 형벌(벌칙)을 정할 때에도 개별적·구체적 위임이 없더라도 법률의 포괄적 위임이 있다면 죄형법정주의에 위배되지 않는다.</p>
                <h4>Ⅲ. 사안의 적용 및 결론 (소결)</h4>
                <p>처음 보는 조례라 하더라도 법률의 위임 근거가 존재하고 자치사무 범위를 넘지 않았다면 포괄위임금지원칙에 위배되지 않아 합헌이다.</p>
            </div>
        </div>
    </div>
    <div class="bottom-bar"></div>
</div>

<!-- PAGE B -->
<div class="page">
    <div class="top-bar"></div>
    <div class="header-area">
        <div class="header-title">
            <span class="badge">주제 B</span> 진정소급입법 vs 부진정소급입법 비교
        </div>
        <div class="header-timer">⏱️ 목표시간: 10분 [서론 2분 | 본론 6분 | 결론 2분]</div>
    </div>
    
    <div class="content-container">
        <div class="center-line"></div>
        
        <!-- LEFT: Blank Writing Area -->
        <div class="column column-left">
            <div class="col-title col-title-left">✍️ 나의 답안 작성란 (서-본-결 시간 안배 훈련)</div>
            <div class="time-guide">
                <strong>💡 [시간 안배 가이드]</strong><br>
                • <strong>서론 (0~2분)</strong>: 형법 제1조 제1항 행위시법주의 및 소급효금지 제시<br>
                • <strong>본론 (2~8분)</strong>: 진정 vs 부진정 개념, 신뢰보호, 허용 여부 서술식 비교<br>
                • <strong>결론 (8~10분)</strong>: 형법 제1조 제2항(재판시법) 예외와 최종 정리
            </div>
            <div class="ruled-lines">
                <!-- Blank lines for student writing -->
            </div>
        </div>
        
        <!-- RIGHT: Model Answer -->
        <div class="column column-right">
            <div class="col-title col-title-right">🎓 교수님 스타일 A+ 모범 답안</div>
            <div class="ruled-lines model-answer">
                <h4>Ⅰ. 문제의 제기 (서론)</h4>
                <p>형법 제1조 제1항은 행위시법주의를 규정하여 사후법에 의한 처벌을 금지한다. 이때 진정·부진정소급입법의 구별과 허용성이 문제된다.</p>
                <h4>Ⅱ. 진정 vs 부진정 소급입법 서술식 비교 (본론)</h4>
                <p>1. <strong>진정소급입법:</strong> 이미 <u>완성·종료된 사실관계</u>에 사후법을 적용하는 입법이다. 국민의 신뢰보호 및 법적 안정성을 침해하므로 <u>원칙적 위헌(금지)</u>이다. (단, 피고인에게 유리한 경과 규정 등 예외적 허용)</p>
                <p>2. <strong>부진정소급입법:</strong> 현재 <u>진행 중인 사실관계</u>에 개정 법률을 적용하는 입법이다. 원칙적으로 <u>허용</u>되나, 개인의 신뢰이익과 공익을 형량하여 제한된다.</p>
                <h4>Ⅲ. 사안의 적용 및 결론 (소결)</h4>
                <p>범죄 후 법률 변경으로 형이 경감되거나 폐지된 경우 형법 제1조 제2항에 따라 재판시법을 적용하여 피고인에게 유리하게 판단한다.</p>
            </div>
        </div>
    </div>
    <div class="bottom-bar"></div>
</div>

<!-- PAGE C -->
<div class="page">
    <div class="top-bar"></div>
    <div class="header-area">
        <div class="header-title">
            <span class="badge">주제 C</span> 개재사정 존재 시 상당인과관계 판단
        </div>
        <div class="header-timer">⏱️ 목표시간: 12분 [서론 2분 | 본론 8분 | 결론 2분]</div>
    </div>
    
    <div class="content-container">
        <div class="center-line"></div>
        
        <!-- LEFT: Blank Writing Area -->
        <div class="column column-left">
            <div class="col-title col-title-left">✍️ 나의 답안 작성란 (서-본-결 시간 안배 훈련)</div>
            <div class="time-guide">
                <strong>💡 [시간 안배 가이드]</strong><br>
                • <strong>서론 (0~2분)</strong>: 선행행위, 개재사정(제3자·피해자), 결과 간 인과관계 문제 설정<br>
                • <strong>본론 (2~10분)</strong>: 상당인과관계설 및 예견가능성 판단 기준 서술<br>
                • <strong>결론 (10~12분)</strong>: 인과관계 단절 여부 및 최종 죄책 귀속
            </div>
            <div class="ruled-lines">
                <!-- Blank lines for student writing -->
            </div>
        </div>
        
        <!-- RIGHT: Model Answer -->
        <div class="column column-right">
            <div class="col-title col-title-right">🎓 교수님 스타일 A+ 모범 답안</div>
            <div class="ruled-lines model-answer">
                <h4>Ⅰ. 문제의 제기 (서론)</h4>
                <p>행위자의 선행행위 이후 피해자의 특이체질이나 제3자의 행위 등 개재사정이 개입하여 결과가 발생한 경우 인과관계 인정 여부가 다퉈진다.</p>
                <h4>Ⅱ. 개재사정과 상당인과관계 법리 (본론)</h4>
                <p>1. <strong>상당인과관계의 의의:</strong> 형법상 인과관계는 조건관계뿐만 아니라 경험칙상 '상당성'이 인정되어야 결과에 대한 책임을 물을 수 있다.</p>
                <p>2. <strong>개재사정 시 판단 기준 (예견가능성):</strong> 선행행위에 비추어 개재사정이 통상 예견 가능한 범위 내라면 인과관계가 <u>유지</u>된다. 반면, 이례적이고 독립적인 원인에 기인한 경우 인과관계는 <u>단절</u>된다.</p>
                <p>3. <strong>판례의 태도:</strong> 김밥·콜라 사건, 특이체질 사건 등에서 피고인의 선행 상해행위와 결과 사이 통상 예견 가능성이 있다면 결과에 대한 책임을 인정한다.</p>
                <h4>Ⅲ. 사안의 적용 및 결론 (소결)</h4>
                <p>개재사정을 예견할 수 있었다면 상당인과관계가 인정되어 결과반가치에 대한 책임이 피고인에게 귀속된다.</p>
            </div>
        </div>
    </div>
    <div class="bottom-bar"></div>
</div>

<!-- PAGE D -->
<div class="page">
    <div class="top-bar"></div>
    <div class="header-area">
        <div class="header-title">
            <span class="badge">주제 D</span> 작위와 부작위의 경합 (이리역/세월호 스타일)
        </div>
        <div class="header-timer">⏱️ 목표시간: 15분 [서론 2분 | 본론 10분 | 결론 3분]</div>
    </div>
    
    <div class="content-container">
        <div class="center-line"></div>
        
        <!-- LEFT: Blank Writing Area -->
        <div class="column column-left">
            <div class="col-title col-title-left">✍️ 나의 답안 작성란 (서-본-결 시간 안배 훈련)</div>
            <div class="time-guide">
                <strong>💡 [시간 안배 가이드]</strong><br>
                • <strong>서론 (0~2분)</strong>: 행위의 분할 (제1행위: 과실작위 / 제2행위: 고의부작위)<br>
                • <strong>본론 (2~12분)</strong>: 보증인의 지위, 행위동가성, 작위 vs 부작위 구별 및 경합 법리<br>
                • <strong>결론 (12~15분)</strong>: 형량 우위의 고의부작위범 흡수/우선 적용 소결
            </div>
            <div class="ruled-lines">
                <!-- Blank lines for student writing -->
            </div>
        </div>
        
        <!-- RIGHT: Model Answer -->
        <div class="column column-right">
            <div class="col-title col-title-right">🎓 교수님 스타일 A+ 모범 답안</div>
            <div class="ruled-lines model-answer">
                <h4>Ⅰ. 행위의 분할 및 문제의 제기 (서론)</h4>
                <p>본 사안에서 피고인의 행위는 ① 위험을 유발한 [선행 과실작위]와 ② 위험 발생 후 구호 조치를 이행하지 않은 [후행 고의부작위]로 분할된다.</p>
                <h4>Ⅱ. 작위와 부작위 경합의 법리 (본론)</h4>
                <p>1. <strong>선행행위로 인한 보증인의 지위:</strong> 위험한 선행행위로 위험을 야기한 자는 결과를 방지해야 할 법적 작위의무(보증인의 지위)를 진다.</p>
                <p>2. <strong>부진정부작위범의 성립요건:</strong> 작위의무 불이행이 작위에 의한 실행행위와 법적 가치가 동등(행위동가성)해야 한다.</p>
                <p>3. <strong>경합 시 해결책 (형량 우위 원칙):</strong> 과실작위범과 고의부작위범이 경합할 때, 법정형과 비난가능성이 훨씬 무거운 <u>고의의 부작위범이 우선 적용</u>된다.</p>
                <h4>Ⅲ. 사안의 적용 및 결론 (소결)</h4>
                <p>피고인은 보증인의무를 고의로 불이행하였으므로 과실범을 넘어 형량이 무거운 부작위범(치사/살인)의 죄책을 진다.</p>
            </div>
        </div>
    </div>
    <div class="bottom-bar"></div>
</div>

<!-- PAGE E -->
<div class="page">
    <div class="top-bar"></div>
    <div class="header-area">
        <div class="header-title">
            <span class="badge">주제 E</span> 정당방위의 성립 요건 (최말자 사건 스타일)
        </div>
        <div class="header-timer">⏱️ 목표시간: 15분 [서론 2분 | 본론 10분 | 결론 3분]</div>
    </div>
    
    <div class="content-container">
        <div class="center-line"></div>
        
        <!-- LEFT: Blank Writing Area -->
        <div class="column column-left">
            <div class="col-title col-title-left">✍️ 나의 답안 작성란 (서-본-결 시간 안배 훈련)</div>
            <div class="time-guide">
                <strong>💡 [시간 안배 가이드]</strong><br>
                • <strong>서론 (0~2분)</strong>: 형법 제21조 제1항 제시 및 정당방위 요건 문제 설정<br>
                • <strong>본론 (2~12분)</strong>: 현재의 부당한 침해, 방위의사, 상당한 이유(완화된 기준) 서술<br>
                • <strong>결론 (12~15분)</strong>: 과잉방위 배제 및 위법성조각(무죄) 최종 소결
            </div>
            <div class="ruled-lines">
                <!-- Blank lines for student writing -->
            </div>
        </div>
        
        <!-- RIGHT: Model Answer -->
        <div class="column column-right">
            <div class="col-title col-title-right">🎓 교수님 스타일 A+ 모범 답안</div>
            <div class="ruled-lines model-answer">
                <h4>Ⅰ. 문제의 제기 (서론)</h4>
                <p>피해자가 성폭력 범죄 등 급박한 침해 상황에서 가해자에게 상해를 입힌 행위가 형법 제21조 제1항의 정당방위에 해당하는지 다퉈진다.</p>
                <h4>Ⅱ. 정당방위의 3대 요건 및 법리 (본론)</h4>
                <p>1. <strong>현재의 부당한 침해:</strong> 강간·추행 등의 범행 시도는 성적 자기결정권에 대한 현재의 부당한 침해이다.</p>
                <p>2. <strong>방위의사:</strong> 침해를 인식하고 이를 방어하려는 주관적 방위의사가 존재해야 한다.</p>
                <p>3. <strong>상당한 이유 (판례의 완화 기준):</strong> 공포와 당황 속에서 이루어진 여성의 저항 행위는 수단의 상당성을 엄격히 따지지 않고 사회상규상 '상당한 이유'를 넓게 인정한다.</p>
                <h4>Ⅲ. 사안의 적용 및 결론 (소결)</h4>
                <p>피고인의 반항 행위는 정당방위의 요건을 모두 충족하여 위법성이 조각되므로 무죄이다. (과잉방위 미적용)</p>
            </div>
        </div>
    </div>
    <div class="bottom-bar"></div>
</div>

</body>
</html>
"""

html_path = "/mnt/data/criminal_law_essay_test_sheets.html"
pdf_path = "/mnt/data/criminal_law_essay_test_sheets.pdf"

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

HTML(filename=html_path).write_pdf(pdf_path)
print("PDF generated successfully.")