import React, { useEffect } from "react";
import DragDrop from "./DragDrop";
import { ImgComparisonSlider } from '@img-comparison-slider/react';
import { useState } from "react";
import Tick from "../assets/correct.png";

const DetectSymmetry = () => {

    const [File, setFile] = useState(null);
    const [receivedImage, setReceivedImage] = useState(null); // State for storing actual image
    const [message, setMessage] = useState(''); // State for storing status message

    const resetUpload = () => {
        setFile(null);
        setReceivedImage(null);
        setPreviewUrl(null);
        setMessage('');
    };


    const [previewUrl, setPreviewUrl] = useState(null); // State for the image preview URL

    const sendFile = async (File) => {
        const formData = new FormData();
        formData.append('image', File);

        try {
            const response = await fetch('http://localhost:5001/process_image', {
                method: 'POST',
                body: formData,
            });

            const data = await response.json();
            // Process your response data here

            if (data.image) {
                setReceivedImage(`data:image/jpeg;base64,${data.image}`);
            }

            if (data.message) {
                setMessage(data.message);
            }

        } catch (error) {
            console.error('Error uploading image:', error);
        }

    }


    useEffect(() => {
        if (!File) {
            setPreviewUrl(null);
            return;
        }



        const fileUrl = URL.createObjectURL(File);
        setPreviewUrl(fileUrl);

        sendFile(File)


        return () => {
            URL.revokeObjectURL(fileUrl);
        };
    }, [File]);

    return (

        <div className="flex flex-col h-full w-full py-10 px-10 items-center">
            <div className="flex justify-center">
                <h1 className="text-5xl font-monteserrat font-semibold text-[#245870] mt-[2rem] drop-shadow-md">Detect Facial Paralysis</h1>
            </div>
            <div className="flex flex-col h-full w-full items-center">
                {!File ? (
                    <>
                        <DragDrop setPicture={setFile} />
                        <div className="w-[70%] h-[20%] flex justify-between mt-4 text-[#245870]">
                            <h1 className="text-md font-poppins w-[60%]">
                                Delve into the pioneering realm of our Facial Paralysis AI Detection Suite. With meticulous precision, our AI scans the human countenance, unveiling the subtlest nuances of asymmetry. It's where cutting-edge technology meets compassionate care, empowering users with swift, non-invasive diagnostics. Engage with an interface where every line, every contour, every shade is analyzed with empathetic accuracy.
                            </h1>
                            <div className="flex flex-col">
                                <h1 className="text-sm font-poppins mb-4">
                                    <img src={Tick} alt="tick" className="h-6 w-6 inline-block mr-2" />
                                    For Mac, Windows, Linux, iOS, and Android
                                </h1>
                                <h1 className="text-sm font-poppins mb-4">
                                    <img src={Tick} alt="tick" className="h-6 w-6 inline-block mr-2" />
                                    Non-intrusive analysis of facial features
                                </h1>
                                <h1 className="text-sm font-poppins mb-4">
                                    <img src={Tick} alt="tick" className="h-6 w-6 inline-block mr-2" />
                                    Instant facial symmetry analysis with AI
                                </h1>

                            </div>


                        </div>
                    </>) : (
                    <div div className="flex justify-center items-center mt-4 flex-col max-h-[40rem]">
                        {receivedImage &&
                            <ImgComparisonSlider className="border-8 border-[#245870] rounded-md" >
                                <img slot="first" src={previewUrl} className="h-[35rem]" />
                                <img slot="second" src={receivedImage} className="h-[35rem]" />
                            </ImgComparisonSlider>
                        }
                        {message &&
                            <div >

                                <div className="rounded-full mt-[2rem] bg-[#3aa4be] text-white text-2xl py-[1.5rem] font-poppins font-bold px-[2rem] h-[2.5rem] justify-center items-center flex drop-shadow-lg ">
                                    {message}


                                </div>
                                <button onClick={resetUpload} className="rounded-full bg-[#245870] text-white text-lg py-2 px-4 mt-4 hover:bg-[#1b4153] transition duration-300 ease-in-out absolute bottom-[2rem] left-[87vw]">
                                    Upload Another
                                </button>
                            </div>

                        }

                    </div>
                )}

            </div>
        </div >
    );
};
export default DetectSymmetry;
