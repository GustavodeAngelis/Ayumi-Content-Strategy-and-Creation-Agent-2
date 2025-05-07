# Testing Guide

## 🎯 Testing Strategy

### 1. Test Types
- Unit Tests: Test individual components
- Integration Tests: Test component interactions
- End-to-End Tests: Test complete user flows
- Performance Tests: Test system performance
- Security Tests: Test security measures

### 2. Test Coverage Goals
- Backend: 80%+ coverage
- Frontend: 70%+ coverage
- Critical paths: 100% coverage

## 🧪 Backend Testing

### 1. Unit Testing
```python
# Example test structure
import pytest
from fastapi.testclient import TestClient
from app.models import Content
from app.services import ContentService

def test_content_generation():
    # Arrange
    service = ContentService()
    prompt = "Test prompt"
    
    # Act
    result = service.generate_content(prompt)
    
    # Assert
    assert result is not None
    assert isinstance(result, Content)
    assert len(result.content) > 0
```

### 2. Integration Testing
```python
# Example integration test
async def test_content_workflow():
    async with AsyncClient(app=app, base_url="http://test") as client:
        # Create content
        response = await client.post(
            "/api/v1/content/generate",
            json={"prompt": "Test prompt"}
        )
        assert response.status_code == 200
        content_id = response.json()["id"]
        
        # Get content
        response = await client.get(f"/api/v1/content/{content_id}")
        assert response.status_code == 200
        assert response.json()["content"] is not None
```

### 3. Performance Testing
```python
# Example performance test
def test_content_generation_performance():
    service = ContentService()
    start_time = time.time()
    
    # Generate multiple contents
    for _ in range(10):
        service.generate_content("Test prompt")
    
    end_time = time.time()
    assert (end_time - start_time) < 5.0  # Should complete within 5 seconds
```

## 🎨 Frontend Testing

### 1. Component Testing
```typescript
// Example component test
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { ContentEditor } from './ContentEditor';

describe('ContentEditor', () => {
    it('should update content on user input', async () => {
        // Arrange
        const onUpdate = jest.fn();
        render(<ContentEditor onUpdate={onUpdate} />);
        
        // Act
        const input = screen.getByRole('textbox');
        await userEvent.type(input, 'New content');
        
        // Assert
        expect(input).toHaveValue('New content');
        expect(onUpdate).toHaveBeenCalled();
    });
});
```

### 2. Integration Testing
```typescript
// Example integration test
describe('Content Workflow', () => {
    it('should create and display content', async () => {
        // Arrange
        render(<App />);
        
        // Act
        await userEvent.click(screen.getByText('Create Content'));
        await userEvent.type(screen.getByLabelText('Prompt'), 'Test prompt');
        await userEvent.click(screen.getByText('Generate'));
        
        // Assert
        expect(await screen.findByText('Generated Content')).toBeInTheDocument();
    });
});
```

### 3. E2E Testing
```typescript
// Example E2E test using Cypress
describe('Content Creation', () => {
    it('should create and publish content', () => {
        cy.visit('/');
        cy.get('[data-testid="create-content"]').click();
        cy.get('[data-testid="prompt-input"]').type('Test prompt');
        cy.get('[data-testid="generate-button"]').click();
        cy.get('[data-testid="content-preview"]').should('be.visible');
        cy.get('[data-testid="publish-button"]').click();
        cy.get('[data-testid="success-message"]').should('be.visible');
    });
});
```

## 📊 Test Coverage

### 1. Backend Coverage
```bash
# Run tests with coverage
pytest --cov=app tests/
```

### 2. Frontend Coverage
```bash
# Run tests with coverage
npm test -- --coverage
```

## 🔍 Test Data

### 1. Fixtures
```python
# Example fixture
@pytest.fixture
def sample_content():
    return {
        "prompt": "Test prompt",
        "context": {
            "audience": "artists",
            "tone": "educational"
        }
    }
```

### 2. Mock Data
```python
# Example mock
from unittest.mock import Mock

def test_with_mock():
    mock_service = Mock()
    mock_service.generate_content.return_value = "Mocked content"
    
    result = mock_service.generate_content("Test prompt")
    assert result == "Mocked content"
```

## 🚀 Running Tests

### 1. Local Development
```bash
# Backend
pytest

# Frontend
npm test
```

### 2. CI/CD Pipeline
```yaml
# Example GitHub Actions workflow
name: Tests
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Run tests
        run: |
          pytest
          npm test
```

## 📝 Test Documentation

### 1. Test Cases
- Document test scenarios
- Include test data
- Document expected results
- Note edge cases

### 2. Test Reports
- Generate test reports
- Track coverage metrics
- Document test failures
- Maintain test history

## 🔒 Security Testing

### 1. Authentication Tests
```python
def test_authentication():
    client = TestClient(app)
    response = client.post(
        "/api/v1/content/generate",
        headers={"Authorization": "Bearer invalid-token"}
    )
    assert response.status_code == 401
```

### 2. Authorization Tests
```python
def test_authorization():
    client = TestClient(app)
    response = client.get(
        "/api/v1/admin/users",
        headers={"Authorization": f"Bearer {user_token}"}
    )
    assert response.status_code == 403
```

## 📈 Performance Testing

### 1. Load Testing
```python
def test_load():
    client = TestClient(app)
    start_time = time.time()
    
    # Simulate multiple requests
    for _ in range(100):
        client.get("/api/v1/content")
    
    end_time = time.time()
    assert (end_time - start_time) < 10.0
```

### 2. Stress Testing
```python
def test_stress():
    client = TestClient(app)
    
    # Simulate concurrent requests
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [
            executor.submit(client.get, "/api/v1/content")
            for _ in range(100)
        ]
        results = [f.result() for f in futures]
    
    assert all(r.status_code == 200 for r in results)
``` 