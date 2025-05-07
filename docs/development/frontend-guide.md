# Frontend Development Guide

## 🎯 Frontend Architecture

### 1. Technology Stack
- React 18+
- TypeScript 4+
- Next.js 13+
- Tailwind CSS
- React Query
- Zustand (State Management)

### 2. Project Structure
```
frontend/
├── src/
│   ├── components/     # Reusable components
│   ├── pages/         # Page components
│   ├── hooks/         # Custom hooks
│   ├── store/         # State management
│   ├── services/      # API services
│   ├── utils/         # Utility functions
│   ├── types/         # TypeScript types
│   └── styles/        # Global styles
├── public/            # Static assets
└── tests/            # Test files
```

## 📝 Component Development

### 1. Component Structure
```typescript
// Example component
import { useState } from 'react';
import { useQuery } from 'react-query';
import type { Content } from '@/types';

interface ContentEditorProps {
    initialContent?: Content;
    onSave: (content: Content) => void;
}

export const ContentEditor: React.FC<ContentEditorProps> = ({
    initialContent,
    onSave
}) => {
    const [content, setContent] = useState(initialContent);
    
    // Implementation
    return (
        <div className="content-editor">
            {/* Component JSX */}
        </div>
    );
};
```

### 2. Styling Guidelines
```typescript
// Example styled component
const StyledButton = styled.button`
    background-color: ${props => props.theme.colors.primary};
    padding: 0.5rem 1rem;
    border-radius: 0.25rem;
    
    &:hover {
        background-color: ${props => props.theme.colors.primaryDark};
    }
`;
```

## 🔄 State Management

### 1. Local State
```typescript
// Using useState
const [content, setContent] = useState<Content | null>(null);

// Using useReducer
const [state, dispatch] = useReducer(contentReducer, initialState);
```

### 2. Global State
```typescript
// Using Zustand
import create from 'zustand';

interface ContentStore {
    content: Content[];
    addContent: (content: Content) => void;
    removeContent: (id: string) => void;
}

const useContentStore = create<ContentStore>((set) => ({
    content: [],
    addContent: (content) => 
        set((state) => ({ content: [...state.content, content] })),
    removeContent: (id) =>
        set((state) => ({
            content: state.content.filter((c) => c.id !== id)
        }))
}));
```

## 📡 API Integration

### 1. API Client
```typescript
// Example API client
import axios from 'axios';

const api = axios.create({
    baseURL: process.env.NEXT_PUBLIC_API_URL,
    headers: {
        'Content-Type': 'application/json'
    }
});

export const contentApi = {
    generate: async (prompt: string) => {
        const response = await api.post('/content/generate', { prompt });
        return response.data;
    },
    
    getContent: async (id: string) => {
        const response = await api.get(`/content/${id}`);
        return response.data;
    }
};
```

### 2. React Query Integration
```typescript
// Example query hook
export const useContent = (id: string) => {
    return useQuery(['content', id], () => contentApi.getContent(id), {
        staleTime: 5 * 60 * 1000, // 5 minutes
        cacheTime: 30 * 60 * 1000 // 30 minutes
    });
};
```

## 🎨 UI/UX Guidelines

### 1. Design System
```typescript
// Theme configuration
export const theme = {
    colors: {
        primary: '#007AFF',
        secondary: '#5856D6',
        success: '#34C759',
        error: '#FF3B30'
    },
    spacing: {
        xs: '0.25rem',
        sm: '0.5rem',
        md: '1rem',
        lg: '1.5rem',
        xl: '2rem'
    },
    typography: {
        h1: '2rem',
        h2: '1.5rem',
        body: '1rem',
        small: '0.875rem'
    }
};
```

### 2. Component Library
```typescript
// Example button component
interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
    variant?: 'primary' | 'secondary' | 'outline';
    size?: 'sm' | 'md' | 'lg';
}

export const Button: React.FC<ButtonProps> = ({
    variant = 'primary',
    size = 'md',
    children,
    ...props
}) => {
    return (
        <button
            className={`btn btn-${variant} btn-${size}`}
            {...props}
        >
            {children}
        </button>
    );
};
```

## 🧪 Testing

### 1. Component Testing
```typescript
// Example component test
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { ContentEditor } from './ContentEditor';

describe('ContentEditor', () => {
    it('should update content on user input', async () => {
        const onSave = jest.fn();
        render(<ContentEditor onSave={onSave} />);
        
        const input = screen.getByRole('textbox');
        await userEvent.type(input, 'New content');
        
        expect(input).toHaveValue('New content');
    });
});
```

### 2. Integration Testing
```typescript
// Example integration test
describe('Content Workflow', () => {
    it('should create and save content', async () => {
        render(<App />);
        
        await userEvent.click(screen.getByText('Create Content'));
        await userEvent.type(screen.getByLabelText('Content'), 'Test content');
        await userEvent.click(screen.getByText('Save'));
        
        expect(await screen.findByText('Content saved')).toBeInTheDocument();
    });
});
```

## 📱 Responsive Design

### 1. Breakpoints
```typescript
// Breakpoint configuration
export const breakpoints = {
    sm: '640px',
    md: '768px',
    lg: '1024px',
    xl: '1280px',
    '2xl': '1536px'
};
```

### 2. Media Queries
```typescript
// Example responsive component
const ResponsiveContainer = styled.div`
    padding: 1rem;
    
    @media (min-width: ${breakpoints.md}) {
        padding: 2rem;
    }
    
    @media (min-width: ${breakpoints.lg}) {
        padding: 3rem;
    }
`;
```

## 🔒 Security

### 1. Authentication
```typescript
// Example auth hook
export const useAuth = () => {
    const [user, setUser] = useState<User | null>(null);
    
    const login = async (credentials: Credentials) => {
        const response = await authApi.login(credentials);
        setUser(response.user);
    };
    
    const logout = () => {
        setUser(null);
    };
    
    return { user, login, logout };
};
```

### 2. Authorization
```typescript
// Example protected route
export const ProtectedRoute: React.FC<{ children: React.ReactNode }> = ({
    children
}) => {
    const { user } = useAuth();
    
    if (!user) {
        return <Navigate to="/login" />;
    }
    
    return <>{children}</>;
};
```

## 📈 Performance Optimization

### 1. Code Splitting
```typescript
// Example dynamic import
const ContentEditor = dynamic(() => import('./ContentEditor'), {
    loading: () => <LoadingSpinner />
});
```

### 2. Memoization
```typescript
// Example memoized component
export const MemoizedContent = React.memo(({ content }: ContentProps) => {
    return (
        <div className="content">
            {content}
        </div>
    );
});
```

## 🚀 Deployment

### 1. Build Process
```bash
# Production build
npm run build

# Development build
npm run dev
```

### 2. Environment Configuration
```typescript
// Environment variables
export const config = {
    apiUrl: process.env.NEXT_PUBLIC_API_URL,
    environment: process.env.NODE_ENV,
    version: process.env.NEXT_PUBLIC_VERSION
};
``` 