import "./Dashboard.css";
import React, { useState, useEffect } from 'react';
import { FaDoorOpen, FaMailBulk, FaRunning } from "react-icons/fa";
import { useNavigate } from "react-router-dom";
import StatsChart from '../Components/StatsChart';
import UserList from '../Components/UserList';
import AdminInfos from "../Components/AdminInfos";
import { getCsrfToken } from "../utils/csrf"; // Function for csrf
import { getBackEndDomain } from "../utils/backend-domain";
import ChoicePopUp from "../Components/ChoicePopUp";

const Info = () => {
  return (
    <>
        <h1>Will follow!</h1>
    </>
  );
};

export default Info;