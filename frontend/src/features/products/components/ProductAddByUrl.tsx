import React from "react";
import backgound from "../../../assets/sm3.jpg";
import styled from "styled-components";
import { useState } from "react";
import { useAddProductByUrl } from "../hooks/useAddProductByUrl";

export default function TrackSearch() {
  const [url, setUrl] = useState("");
  const { submit, loading, error, success } = useAddProductByUrl();

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    submit(url);
  };

  const SearchbarButton = styled.button`
    height: 42px;
    width: 110px;
    border-radius: 26px;
    background: #ff6a00;
    color: white;
    font-weight: 600;
    border: none;
    cursor: pointer;

    &:hover {
      background: #e85f00;
    }
  `;

  const StyledForm = styled.form`
    display: flex;
    background-color: aliceblue;
    border-radius: 30px;
    height: 50px;
    align-items: center;
    margin-right: 1rem;
  `;

  return (
    <section className="relative w-full min-w-[1280px]">
      {/* HERO */}
      <div className="relative h-[515px] w-full overflow-hidden">
        {/* Background image */}
        <img
          src={backgound}
          alt=""
          className="absolute inset-0 w-[1920px] h-[624px] object-cover"
        />

        {/* Content container */}
        <div className="relative mx-auto flex h-full w-[1440px] items-center">
          <div className="mt-[189px] px-8">
            {/* Title */}
            <h1 className="flex flex-col text-[44px] font-bold leading-[72px] text-white max-w-[950px]">
              Unleash the Power of
              <span className="text-primary">PriceWise</span>
            </h1>

            {/* Search */}
            <div className="mt-8 w-[786px] h-[140px]">
              <div className="mt-12 px-8">
                <StyledForm onSubmit={handleSubmit}>
                  <div className="relative w-full">
                    <input
                      type="text"
                      placeholder="ใส่ลิงก์สินค้าที่ต้องการ"
                      className="border border-gray-300 px-3 py-3 rounded-[30px] w-full pr-[140px] bg-transparent"
                      onChange={(e) => setUrl(e.target.value)}
                    />
                    {/* 4 to 3   */}

                    <SearchbarButton
                      type="submit"
                      className="absolute right-2 top-1/2 -translate-y-1/2"
                    >
                      ค้นหา
                    </SearchbarButton>
                  </div>
                </StyledForm>
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* TRENDING */}
      <section className="mx-auto mt-20 w-[1440px]">
        <h2 className="mb-10 text-2xl font-semibold">Trending</h2>
        <div className="flex flex-wrap gap-x-8 gap-y-16"></div>
      </section>
    </section>
  );
}
