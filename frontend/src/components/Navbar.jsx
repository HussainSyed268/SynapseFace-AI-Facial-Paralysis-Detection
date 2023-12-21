import React from "react";
import { Link } from "react-router-dom";

const Navbar = () => {
    return (
        <div className="navbar bg-white h-[10vh] text-[#1d475b] drop-shadow-lg">
            <div className="navbar-start">
                <div className="dropdown">
                    <div tabIndex={0} role="button" className="btn btn-ghost lg:hidden">
                        <svg
                            xmlns="http://www.w3.org/2000/svg"
                            className="h-5 w-5"
                            fill="none"
                            viewBox="0 0 24 24"
                            stroke="currentColor"
                        >
                            <path
                                strokeLinecap="round"
                                strokeLinejoin="round"
                                strokeWidth="2"
                                d="M4 6h16M4 12h8m-8 6h16"
                            />
                        </svg>
                    </div>
                    <ul
                        tabIndex={0}
                        className="menu menu-sm dropdown-content mt-3 z-[1] p-2 shadow bg-base-100 rounded-box w-52"
                    >
                        <li>
                            <Link>Item 1</Link>
                        </li>
                        <li>
                            <Link>Parent</Link>
                            <ul className="p-2">
                                <li>
                                    <Link>Submenu 1</Link>
                                </li>
                                <li>
                                    <Link>Submenu 2</Link>
                                </li>
                            </ul>
                        </li>
                        <li>
                            <Link>Item 3</Link>
                        </li>
                    </ul>
                </div>
                <Link className="text-xl font-normal font-poppins flex">
                    SynapseFace
                </Link>
            </div>
            <div className="navbar-center hidden lg:flex">
                <ul className="menu menu-horizontal px-1 text-[#1d475b] font-poppins text-md font-bold">
                    <li className="mr-2 hover:text-[#1494ff] ">
                        <Link >Embed text in Image</Link>
                    </li>

                    <li className="mr-2 hover:text-[#1494ff]">
                        <Link>Embed Image in Image</Link>
                    </li>
                    <li className="mr-2 hover:text-[#1494ff]">
                        <Link>Decode Text from Image</Link>
                    </li>

                    <li className="mr-2 hover:text-[#1494ff]">
                        <Link>Decode Image from Image</Link>
                    </li>
                </ul>
            </div>
            <div className="navbar-end">
                <ul className="menu menu-horizontal px-1 text-md font-bold hover:text-[#1494ff]">
                    <li>
                        <Link>Settings</Link>
                    </li>
                </ul>
                <a className="btn btn-outline btn-info">Sign In</a>
            </div>
        </div>
    );
};
export default Navbar;
