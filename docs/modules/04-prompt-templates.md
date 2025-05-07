# Module 4: Prompt Templates

## Overview

The Prompt Templates module defines the structured prompts used to guide the LLM in generating content that aligns with Ayumi's tone of voice and strategic goals. These templates ensure consistency, quality, and strategic alignment across all generated content.

## Core Templates

### 1. Content Strategy Template
```python
CONTENT_STRATEGY_TEMPLATE = """
You are Ayumi's content strategy assistant. Your goal is to help create engaging, 
authentic content that resonates with artists and creators.

Context:
- Target Audience: {target_audience}
- Content Goals: {content_goals}
- Performance History: {performance_history}

Task:
Generate a content strategy that:
1. Aligns with the target audience's needs
2. Supports the content goals
3. Builds on successful past content
4. Maintains Ayumi's warm, personal tone

Output Format:
{
    "strategy": {
        "themes": List[str],
        "approaches": List[str],
        "tone_guidelines": Dict[str, str]
    },
    "rationale": str
}
"""
```

### 2. Content Generation Template
```python
CONTENT_GENERATION_TEMPLATE = """
You are creating Instagram content for Ayumi, an artist and educator.

Context:
- Theme: {theme}
- Target Audience: {target_audience}
- Reference Content: {reference_content}
- Performance Goals: {performance_goals}

Requirements:
1. Maintain warm, personal tone
2. Include clear value for the audience
3. Align with content strategy
4. Optimize for engagement

Output Format:
{
    "caption": str,
    "hashtags": List[str],
    "visual_elements": List[str],
    "engagement_hooks": List[str]
}
"""
```

### 3. Performance Analysis Template
```python
PERFORMANCE_ANALYSIS_TEMPLATE = """
Analyze the performance of Ayumi's content to identify patterns and opportunities.

Data:
- Content History: {content_history}
- Performance Metrics: {performance_metrics}
- Audience Feedback: {audience_feedback}

Analysis Requirements:
1. Identify successful patterns
2. Spot improvement opportunities
3. Suggest strategic adjustments
4. Maintain data-driven approach

Output Format:
{
    "insights": List[Dict[str, Any]],
    "recommendations": List[Dict[str, Any]],
    "action_items": List[str]
}
"""
```

## Template Management

### 1. Version Control
- Template versioning
- Change tracking
- Performance monitoring
- A/B testing support

### 2. Quality Assurance
- Output validation
- Tone consistency checks
- Strategy alignment verification
- Performance impact analysis

### 3. Template Optimization
- Performance-based refinement
- User feedback integration
- Strategy alignment updates
- Tone calibration

## Implementation Guidelines

### 1. Template Usage
```python
class PromptManager:
    def __init__(self):
        self.templates = {
            "strategy": CONTENT_STRATEGY_TEMPLATE,
            "generation": CONTENT_GENERATION_TEMPLATE,
            "analysis": PERFORMANCE_ANALYSIS_TEMPLATE
        }
    
    def format_prompt(self, template_name: str, **kwargs) -> str:
        template = self.templates[template_name]
        return template.format(**kwargs)
```

### 2. Quality Control
```python
class QualityChecker:
    def validate_output(self, output: Dict, template_type: str) -> bool:
        # Implementation details
        pass
    
    def check_tone_alignment(self, content: str) -> float:
        # Implementation details
        pass
```

## Best Practices

1. **Template Design**
   - Clear structure and format
   - Explicit requirements
   - Context inclusion
   - Output validation

2. **Prompt Engineering**
   - Consistent tone
   - Clear instructions
   - Relevant examples
   - Performance optimization

3. **Quality Control**
   - Output validation
   - Tone consistency
   - Strategy alignment
   - Performance tracking

## Future Improvements

- [ ] Implement dynamic template selection
- [ ] Add template performance tracking
- [ ] Enhance tone calibration
- [ ] Improve context integration 