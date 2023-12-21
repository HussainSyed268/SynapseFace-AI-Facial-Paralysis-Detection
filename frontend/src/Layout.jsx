import React from "react";
import Navbar from "./components/Navbar";
import Content from "./Content";

const Layout = () => {
    return (
        <div className="flex flex-col">
            <Navbar />
            <Content />
        </div>
    );
}
export default Layout;