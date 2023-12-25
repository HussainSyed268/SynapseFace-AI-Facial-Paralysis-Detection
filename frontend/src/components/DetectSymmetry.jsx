import React, { useEffect } from "react";
import DragDrop from "./DragDrop";
import { useState } from "react";
import Tick from "../assets/correct.png";

const DetectSymmetry = () => {

    const [File, setFile] = useState(null);

    const [previewUrl, setPreviewUrl] = useState(null); // State for the image preview URL

    const sendFile = async (File) => {
        const formData = new FormData();
        const uploaded = URL.createObjectURL(File);
        formData.append('image', uploaded);
        console.log(formData)

        try {
            const response = await fetch('http://localhost:5000/process_image', {
                method: 'POST',
                body: formData,
            });

            const data = await response.json();
            // Process your response data here
            console.log(data);
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
                <h1 className="text-5xl font-monteserrat font-semibold text-[#245870] mt-[2rem]">Detect Facial Paralysis</h1>
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
                    <div className="flex justify-center items-center mt-4">
                        {previewUrl && (
                            <img src={previewUrl} alt="Uploaded" className="w-[70%] h-[20rem] object-cover" />
                        )}
                    </div>
                )}

            </div>
        </div>
    );
};
export default DetectSymmetry;