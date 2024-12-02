import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
import {
  createBrowserRouter,
  RouterProvider,
} from 'react-router-dom';

import QuickStart from './routes/QuickStart';
import Questions from './routes/Questions';
import Congratulations from './routes/Congratulations';

const router = createBrowserRouter([
  {
    path: "/",
    element: <QuickStart />
  },
  {
	  path: "/questões",
	  element: <Questions />
  },
  {
	  path: "/parabenização",
	  element: <Congratulations />
  }
])

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <RouterProvider router={router} />
  </StrictMode>,
)
