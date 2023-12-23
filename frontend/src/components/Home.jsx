import React from "react";
import Pic from "../assets/Home.png";
import AI from "../assets/AI.png";
import Time from "../assets/real-time.png";
import Precise from "../assets/precise.png";
import Lang from "../assets/lang.png";
import Learn from "../assets/learn.png"

const Home = () => {
    return (
        <div className="flex flex-col h-full w-screen bg-gradient-radial from-[#62b3bd] to-[#133446]">
            <div className=" flex w-full h-[85%]">
                <div className=" flex h-full w-[65%] justify-end items-end">
                    <img src={Pic} alt="Home" className="h-[95%] w-[92%] object-cover" />
                </div>
                <div className=" flex flex-col h-full w-[35%] justify-center items-center">
                    <div className="w-[80%]">
                        <h1
                            className="text-6xl font-monteserrat font-semibold text-white drop-shadow-[0_1.2px_1.2px_rgba(0,0,0,0.8)]
"
                        >
                            Facial Paralysis
                        </h1>
                        <h1
                            className="text-3xl font-monteserrat font-semibold text-white mt-4 drop-shadow-[0_1.2px_1.2px_rgba(0,0,0,0.8)]
"
                        >
                            Detection using AI
                        </h1>
                        <h1
                            className="text-md font-monteserrat font-semibold text-white mt-4 drop-shadow-[0_1.2px_1.2px_rgba(0,0,0,0.8)]
"
                        >
                            Harnessing the Power of Artificial Intelligence to Deliver Accurate, Fast, and Non-invasive Facial Paralysis Detection.
                        </h1>
                        <div className="flex flex-col">
                            <a className="rounded-full bg-white text-[#245870] text-lg font-monteserrat font-bold w-[10rem] h-[3.5rem] flex justify-center items-center my-[1rem]">How it works</a>
                            <a className="rounded-full bg-[#3aa4be] text-white text-xl font-monteserrat font-bold w-[13rem] h-[3.5rem] justify-center items-center flex ">Get Started</a>
                        </div>
                    </div>
                </div>
            </div>
            <div className="flex w-full h-[15%] bg-[#eefbff] justify-around">
                <div className="flex flex-col w-[15%] items-center justify-center ">
                    <img src={AI} alt="AI" className="h-[2.5rem] w-[2.5rem] mx-auto" />
                    <h1 className="text-sm font-monteserrat font-semibold  text-[#245870] mt-2 text-center">AI-Powered</h1>
                    <h1 className="text-xs font-monteserrat  text-[#3aa4be] mt-1 text-center">Facial symmetry analysis</h1>

                </div>
                <div className="flex flex-col w-[15%] items-center justify-center">
                    <img src={Time} alt="Time" className="h-[2.5rem] w-[2.5rem] mx-auto" />
                    <h1 className="text-md font-monteserrat font-semibold  text-[#245870] mt-2 text-center">Real-Time</h1>
                    <h1 className="text-xs font-monteserrat  text-[#3aa4be] mt-1 text-center">Detection for paralysis</h1>

                </div>
                <div className="flex flex-col w-[15%] items-center justify-center">
                    <img src={Precise} alt="Precise" className="h-[2.5rem] w-[2.5rem] mx-auto" />
                    <h1 className="text-md font-monteserrat font-semibold  text-[#245870] mt-2 text-center">Precision AI Analysis</h1>
                    <h1 className="text-xs font-monteserrat  text-[#3aa4be] mt-1 text-center">Using 28 facial features</h1>

                </div>
                <div className="flex flex-col w-[15%] items-center justify-center">
                    <img src={Learn} alt="Learn" className="h-[2.5rem] w-[2.5rem] mx-auto" />
                    <h1 className="text-md font-monteserrat font-semibold  text-[#245870] mt-2 text-center">Continuous Learning Cycle</h1>
                    <h1 className="text-xs font-monteserrat  text-[#3aa4be] mt-1 text-center">for self-improving AI system</h1>


                </div>
                <div className="flex flex-col w-[15%] items-center justify-center">
                    <img src={Lang} alt="Lang" className="h-[2.5rem] w-[2.5rem] mx-auto" />
                    <h1 className="text-md font-monteserrat font-semibold  text-[#245870] mt-2 text-center">Multi-Language Support</h1>
                    <h1 className="text-xs font-monteserrat  text-[#3aa4be] mt-1 text-center">For global userbase</h1>

                </div>


            </div>
        </div>
    );
};
export default Home;
