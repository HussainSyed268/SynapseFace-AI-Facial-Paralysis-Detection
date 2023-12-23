import React from "react";
import { Route, Routes } from "react-router-dom";
import Home from "./components/Home";
import DetectSymmetry from "./components/DetectSymmetry";
export default function AppContent() {
    return (
        <>
            <div
                className="flex justify-center items-center h-[90vh]"
            >
                <Routes>
                    <Route key={"home"} path={"/"} element={<Home />} />
                    <Route key={"detectSymmetry"} path={"/detect-symmetry"} element={<DetectSymmetry />} />

                </Routes>
            </div>
        </>
    );
}
