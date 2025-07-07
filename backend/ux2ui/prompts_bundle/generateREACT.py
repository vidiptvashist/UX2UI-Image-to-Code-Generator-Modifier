import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from ux2ui.models.model import *
from ux2ui.utils.post_processing import *


def generateREACT(html,image_path):
    prompt = """
    # HTML to React + TypeScript Conversion Prompt

    You are an expert React and TypeScript developer. Your task is to convert the provided HTML code into a well-structured React application with TypeScript.

    ## Requirements:

    1. **Convert HTML to React Components**: Transform the HTML into functional React components using TypeScript
    2. **Component Structure**: Break down the HTML into logical, reusable components
    3. **TypeScript Integration**: Add proper TypeScript types, interfaces, and type annotations
    4. **Modern React Patterns**: Use React hooks (useState, useEffect, etc.) where appropriate
    5. **Styling**: Convert inline styles and CSS classes to appropriate React styling approaches
    6. **Event Handlers**: Convert HTML event attributes to React event handlers
    7. **Props and State**: Identify what should be props vs state and type them properly
    8. **File Organization**: Structure the code into appropriate files

    ## Output Format:

    Return the code as a JSON object with filename as key and code content as value. Include ALL necessary files to run a complete React application:

    ```json
    {
    "package.json": "// Package configuration with dependencies",
    "tsconfig.json": "// TypeScript configuration",
    "vite.config.ts": "// Vite build configuration",
    "index.html": "// HTML entry point",
    "src/main.tsx": "// React app entry point",
    "src/App.tsx": "// Main app component",
    "src/components/ComponentName.tsx": "// Individual components",
    "src/types/index.ts": "// Type definitions",
    "src/styles/globals.css": "// Global styles",
    "src/styles/components.css": "// Component styles",
    ".gitignore": "// Git ignore file",
    "README.md": "// Project documentation"
    }
    ```

    ## Required Files to Generate:

    1. **package.json** - Include all necessary dependencies (React, TypeScript, Vite, etc.)
    2. **tsconfig.json** - TypeScript compiler configuration
    3. **vite.config.ts** - Vite bundler configuration for development and build
    4. **index.html** - HTML entry point for the app
    5. **src/main.tsx** - React application entry point
    6. **src/App.tsx** - Main application component
    7. **src/components/** - Individual React components
    8. **src/types/index.ts** - TypeScript type definitions
    9. **src/styles/** - CSS files for styling
    10. **.gitignore** - Git ignore patterns
    11. **README.md** - Project setup and run instructions

    ## Project Structure:
    ```
    project/
    ├── package.json
    ├── tsconfig.json
    ├── vite.config.ts
    ├── index.html
    ├── .gitignore
    ├── README.md
    └── src/
        ├── main.tsx
        ├── App.tsx
        ├── components/
        │   └── ComponentName.tsx
        ├── types/
        │   └── index.ts
        └── styles/
            ├── globals.css
            └── components.css
    ```

    ## Conversion Guidelines:

    - Convert HTML elements to JSX (className instead of class, etc.)
    - Extract reusable components from repeated HTML patterns
    - Add TypeScript interfaces for component props
    - Use appropriate React hooks for interactivity
    - Maintain semantic HTML structure
    - Handle form inputs with controlled components
    - Convert event handlers (onclick → onClick, etc.)
    - Add proper key props for lists
    - Include error handling and loading states where relevant
    - Set up proper development environment with Vite
    - Include all necessary dependencies and scripts
    - Add proper TypeScript configuration for React

    ## Example Input:
    ```html
    <div class="card">
    <h2>User Profile</h2>
    <input type="text" id="username" placeholder="Enter username">
    <button onclick="submitForm()">Submit</button>
    </div>
    ```

    ## Example Output:
    ```json
    {
    "package.json": "{\n  \"name\": \"react-app\",\n  \"private\": true,\n  \"version\": \"0.0.0\",\n  \"type\": \"module\",\n  \"scripts\": {\n    \"dev\": \"vite\",\n    \"build\": \"tsc && vite build\",\n    \"lint\": \"eslint . --ext ts,tsx --report-unused-disable-directives --max-warnings 0\",\n    \"preview\": \"vite preview\"\n  },\n  \"dependencies\": {\n    \"react\": \"^18.2.0\",\n    \"react-dom\": \"^18.2.0\"\n  },\n  \"devDependencies\": {\n    \"@types/react\": \"^18.2.15\",\n    \"@types/react-dom\": \"^18.2.7\",\n    \"@typescript-eslint/eslint-plugin\": \"^6.0.0\",\n    \"@typescript-eslint/parser\": \"^6.0.0\",\n    \"@vitejs/plugin-react\": \"^4.0.3\",\n    \"eslint\": \"^8.45.0\",\n    \"eslint-plugin-react-hooks\": \"^4.6.0\",\n    \"eslint-plugin-react-refresh\": \"^0.4.3\",\n    \"typescript\": \"^5.0.2\",\n    \"vite\": \"^4.4.5\"\n  }\n}",
    "tsconfig.json": "{\n  \"compilerOptions\": {\n    \"target\": \"ES2020\",\n    \"useDefineForClassFields\": true,\n    \"lib\": [\"ES2020\", \"DOM\", \"DOM.Iterable\"],\n    \"module\": \"ESNext\",\n    \"skipLibCheck\": true,\n    \"moduleResolution\": \"bundler\",\n    \"allowImportingTsExtensions\": true,\n    \"resolveJsonModule\": true,\n    \"isolatedModules\": true,\n    \"noEmit\": true,\n    \"jsx\": \"react-jsx\",\n    \"strict\": true,\n    \"noUnusedLocals\": true,\n    \"noUnusedParameters\": true,\n    \"noFallthroughCasesInSwitch\": true\n  },\n  \"include\": [\"src\"],\n  \"references\": [{ \"path\": \"./tsconfig.node.json\" }]\n}",
    "vite.config.ts": "import { defineConfig } from 'vite';\nimport react from '@vitejs/plugin-react';\n\nexport default defineConfig({\n  plugins: [react()],\n});",
    "index.html": "<!doctype html>\n<html lang=\"en\">\n  <head>\n    <meta charset=\"UTF-8\" />\n    <link rel=\"icon\" type=\"image/svg+xml\" href=\"/vite.svg\" />\n    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\" />\n    <title>React App</title>\n  </head>\n  <body>\n    <div id=\"root\"></div>\n    <script type=\"module\" src=\"/src/main.tsx\"></script>\n  </body>\n</html>",
    "src/main.tsx": "import React from 'react';\nimport ReactDOM from 'react-dom/client';\nimport App from './App.tsx';\nimport './styles/globals.css';\n\nReactDOM.createRoot(document.getElementById('root')!).render(\n  <React.StrictMode>\n    <App />\n  </React.StrictMode>,\n);",
    "src/App.tsx": "import React from 'react';\nimport UserProfile from './components/UserProfile';\nimport './styles/components.css';\n\nconst App: React.FC = () => {\n  return (\n    <div className=\"App\">\n      <UserProfile />\n    </div>\n  );\n};\n\nexport default App;",
    "src/components/UserProfile.tsx": "import React, { useState } from 'react';\nimport { UserProfileProps } from '../types';\n\nconst UserProfile: React.FC<UserProfileProps> = () => {\n  const [username, setUsername] = useState<string>('');\n\n  const handleSubmit = () => {\n    console.log('Username:', username);\n  };\n\n  return (\n    <div className=\"card\">\n      <h2>User Profile</h2>\n      <input\n        type=\"text\"\n        value={username}\n        onChange={(e) => setUsername(e.target.value)}\n        placeholder=\"Enter username\"\n      />\n      <button onClick={handleSubmit}>Submit</button>\n    </div>\n  );\n};\n\nexport default UserProfile;",
    "src/types/index.ts": "export interface UserProfileProps {\n  // Add props here if needed\n}",
    "src/styles/globals.css": "* {\n  margin: 0;\n  padding: 0;\n  box-sizing: border-box;\n}\n\nbody {\n  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', sans-serif;\n  line-height: 1.6;\n  color: #333;\n}\n\n#root {\n  min-height: 100vh;\n}",
    "src/styles/components.css": ".card {\n  background: white;\n  border-radius: 8px;\n  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);\n  padding: 20px;\n  margin: 20px;\n  max-width: 400px;\n}\n\n.card h2 {\n  margin-bottom: 15px;\n  color: #2c3e50;\n}\n\n.card input {\n  width: 100%;\n  padding: 10px;\n  border: 1px solid #ddd;\n  border-radius: 4px;\n  margin-bottom: 10px;\n}\n\n.card button {\n  background: #3498db;\n  color: white;\n  border: none;\n  padding: 10px 20px;\n  border-radius: 4px;\n  cursor: pointer;\n}\n\n.card button:hover {\n  background: #2980b9;\n}",
    ".gitignore": "# Logs\nlogs\n*.log\nnpm-debug.log*\nyarn-debug.log*\nyarn-error.log*\npnpm-debug.log*\nlerna-debug.log*\n\nnode_modules\ndist\ndist-ssr\n*.local\n\n# Editor directories and files\n.vscode/*\n!.vscode/extensions.json\n.idea\n.DS_Store\n*.suo\n*.ntvs*\n*.njsproj\n*.sln\n*.sw?\n\n# Environment variables\n.env\n.env.local\n.env.development.local\n.env.test.local\n.env.production.local",
    "README.md": "# React TypeScript App\n\nA React application generated from HTML with TypeScript support.\n\n## Setup\n\n1. Install dependencies:\n```bash\nnpm install\n```\n\n2. Start development server:\n```bash\nnpm run dev\n```\n\n3. Build for production:\n```bash\nnpm run build\n```\n\n## Project Structure\n\n- `src/components/` - React components\n- `src/types/` - TypeScript type definitions\n- `src/styles/` - CSS styles\n- `src/main.tsx` - Application entry point\n- `src/App.tsx` - Main application component\n\n## Technologies Used\n\n- React 18\n- TypeScript\n- Vite\n- CSS3"
    }
    ```


            """
    prompt +=f"""

    INPUT: {html}

            """
    response = generate_from_text_and_image(prompt, image_path)
    return response


def explanationHTML(react_code):
    prompt = f"""
    # High-Level Code Explanation Prompt for Generated React + TypeScript Application

    You are an expert React and TypeScript developer. Your task is to provide a concise, high-level explanation of the React + TypeScript code that was generated from HTML conversion.

    ## Your Role:
    Provide a brief, accessible overview that helps developers quickly understand:
    - **What** the application does
    - **How** it's structured
    - **Key** technologies and patterns used

    ## Explanation Structure:

    ### 1. **Application Summary** (2-3 sentences)
    - What the app does and its main purpose
    - Key technologies used (React, TypeScript, Vite)

    ### 2. **Project Structure** (bullet points)
    - **Configuration**: package.json, tsconfig.json, vite.config.ts
    - **Source Code**: Components, types, styles
    - **Entry Points**: index.html, main.tsx, App.tsx

    ### 3. **Key Components** (1-2 sentences each)
    - Main components and their purpose
    - How they work together

    ### 4. **TypeScript Integration** (brief overview)
    - Type definitions and interfaces
    - Benefits of type safety

    ### 5. **Development Setup** (quick steps)
    - How to install and run
    - Available npm scripts

    ## Explanation Style:
    - **Concise**: Keep explanations short and to the point
    - **High-Level**: Focus on concepts, not implementation details
    - **Practical**: Include just enough to get started
    - **Accessible**: Use simple language, avoid jargon

    ## Output Format:
    Provide a brief explanation in markdown format with:
    - Clear, short sections
    - Bullet points for lists
    - Minimal code examples (only if essential)
    - Quick reference information

    ## What NOT to Include:
    - Detailed code analysis
    - Line-by-line explanations
    - Deep technical concepts
    - Extensive best practices discussions
    - Complex configuration details

    ## Target Length:
    - Total explanation should be 300-500 words
    - Each section should be 2-4 sentences max
    - Focus on the essentials only

    INPUT: 
        {react_code}
            """
    response = generate_from_text(prompt)
    return response


from ux2ui.prompts_bundle.generateHTML import *

image_path = r"C:\Users\Vidipt\Desktop\project\ui2ux\backend\ux2ui\sample_ux\sample00.png"
html_code = generateHTML(image_path)
response = generateREACT(html_code,image_path)
response =  process_react(response)
print(response)
app_name = "demo"
save_files(app_name, response)


