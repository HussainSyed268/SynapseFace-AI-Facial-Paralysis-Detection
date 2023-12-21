import React from "react";
import { Route, Routes } from "react-router-dom";
import Home from "./components/Home";
export default function AppContent() {
    return (
        <>
            <div
                className="flex justify-center items-center h-[92vh]"
            >
                <Routes>
                    <Route key={"home"} path={"/"} element={<Home />} />

                </Routes>
            </div>
        </>
    );
}
