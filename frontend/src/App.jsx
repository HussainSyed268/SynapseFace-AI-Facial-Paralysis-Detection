import React from "react";
import { BrowserRouter, Route, Routes } from "react-router-dom";

const AppLayout = React.lazy(() => import("./Layout.jsx"));
const Page404 = React.lazy(() => import("./views/Page404.jsx"));

function App() {
  return (
    <div className="App">
      <div className="flex flex-col min-h-screen">
        <BrowserRouter>
          <Routes>
            <Route path="/404" element={<Page404 />} />
            <Route path="*" element={<AppLayout />} />
          </Routes>
        </BrowserRouter>
      </div>
    </div>);
}

export default App;
