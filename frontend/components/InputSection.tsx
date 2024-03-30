import React, { Dispatch, useState } from 'react'

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
  return (
    <div>InputSection</div>
  )
}

export default InputSection