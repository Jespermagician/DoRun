import React from "react";
import PerfectScrollbar from "react-perfect-scrollbar";
import { FaEdit, FaTrash} from "react-icons/fa";
import "react-perfect-scrollbar/dist/css/styles.css";
import "./ListItemUserSelect.css";

const ListItemUserSelect = ({ user }) => {
  return (
    <>
        <ul key={user.iduser} className="list-item">
            <p>Name: {user.firstname} {user.lastname}</p>
            <p>Email: {user.email}</p>
            <p>KM: {user.kilometers}</p>
        </ul>
    </>
  );
};

export default ListItemUserSelect;
