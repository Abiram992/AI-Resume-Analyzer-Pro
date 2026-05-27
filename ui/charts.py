import plotly.express as px
import plotly.graph_objects as go


# =========================
# SKILL BAR CHART
# =========================
def create_skill_chart(skill_data):

    fig = px.bar(
        skill_data,
        x="Skill",
        y="Count",
        title="Skills Overview"
    )

    return fig


# =========================
# RADAR CHART
# =========================
def create_radar_chart(
    skills,
    ats_score
):

    categories = [
        "Technical Skills",
        "Projects",
        "Experience",
        "ATS",
        "Communication"
    ]

    values = [
        min(len(skills) * 10, 100),
        80,
        75,
        ats_score,
        70
    ]

    radar = go.Figure()

    radar.add_trace(
        go.Scatterpolar(
            r=values,
            theta=categories,
            fill='toself',
            name='Resume Score'
        )
    )

    radar.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100]
            )
        ),
        showlegend=False
    )

    return radar