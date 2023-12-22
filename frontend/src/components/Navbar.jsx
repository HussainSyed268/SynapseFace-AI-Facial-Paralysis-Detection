import React from "react";
import { Link } from "react-router-dom";
import Logo from "../assets/logo.png";

const Navbar = () => {
    return (
        <div className="navbar bg-white h-[10vh] text-[#245870] drop-shadow-lg">
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
                <Link className="text-2xl font-normal font-poppins flex text-[#23ddee] justify-center items-center ml-[2rem]">
                    <img src={Logo} alt="logo" className="w-[3.5rem] h-[3.5rem] mr-[1rem]" />
                    SynapseFace
                </Link>
            </div>
            <div className="navbar-center hidden lg:flex">
                <ul className="menu menu-horizontal px-1 text-[#245870] font-poppins text-lg font-bold">
                    <li className="mr-2 hover:text-[#3aa4be] ">
                        <Link >About</Link>
                    </li>

                    <li className="mr-2 hover:text-[#3aa4be]">
                        <Link>How it works</Link>
                    </li>
                    <li className="mr-2 hover:text-[#3aa4be]">
                        <Link>Decode Text from Image</Link>
                    </li>

                    <li className="mr-2 hover:text-[#3aa4be]">
                        <Link>Decode Image from Image</Link>
                    </li>
                </ul>
                <div className="flex">
                    <a className="rounded-full bg-[#e1f2f5] text-[#245870] font-poppins font-bold w-[5rem] flex justify-center items-center mx-[2rem]">Start</a>
                    <a className="rounded-full bg-[#3aa4be] text-white font-poppins font-bold w-[6rem] h-[2.5rem] justify-center items-center flex mr-[2rem]">Sign In</a>
                </div>
            </div>
            {/* <div className="navbar-end">
                <ul className="menu menu-horizontal px-1 text-md font-bold hover:text-[#1494ff]">
                    <li>
                        <Link>Settings</Link>
                    </li>
                </ul>
                <a className="btn btn-outline btn-info">Sign In</a>
            </div> */}
        </div>
    );
};
export default Navbar;
