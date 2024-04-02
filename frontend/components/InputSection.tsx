import React, { Dispatch, useState } from "react";

type InputSectionProps = {
  title: string;
  placeholder: string;
  data: string[] | null;
  setData: Dispatch<React.SetStateAction<string[]>>;
};

function InputSection({
  title,
  placeholder,
  data,
  setData,
}: InputSectionProps) {
  const [inputValue, setInputValue] = useState("");

  const handleAddClick = () => {
    if (inputValue.trim() !== "") {
      setData((prevData) => [...prevData, inputValue]);
      setInputValue("");
    }
  };

  const handleRemoveItem = (index: number) => {
    setData((prevData) =>
      prevData.filter((_, itemIndex) => itemIndex !== index)
    );
  }

  return (
    <div className="mb-4">
        <h2 className="font-bold text-xl">{title}</h2>
        <div className="flex items-center mt-2">
            <input type='text' 
            value={inputValue}
            onChange={(e) => setInputValue(e.target.value)}
            placeholder={placeholder}
            className="p-2 border border-gray-300 rounded-lg w-full mr-2 flex-grow"
            />
            <button
            onClick={handleAddClick}
            className="bg-green-500 hover:bg-green-700 text-white py-2 rounded-lg px-4"
            >Add</button>
        </div>
        <ul>
            {data?.map((item, index) => (
             <li key={index} className="flex items-center mt-2">
                    <span className="p-2 border border-gray-300 rounded-lg w-full mr-2 flex-grow">{item}</span>
                    <button onClick={() => handleRemoveItem(index)} className="bg-red-500 hover:bg-red-700 text-white py-2 rounded-lg px-4">Remove</button>
                </li>    
            ))}
            
        </ul>
    </div>
  );
}

export default InputSection;
