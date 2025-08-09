import React from "react";
import "./Impressum.css"; // CSS-Datei für das Styling
import { useNavigate } from 'react-router-dom';

const DataPrivacy = () => {
    const navigate = useNavigate();
  return (
    <div className="impressum-wrapper">
      <div className="impressum-container">
        <div className="layout-20">
          <div className="layout-20-inner pt-3 pb-2 bg-c2 use-parallax">
            <div className="main-inner">
              <div className="area-20-1 s4">
                <div className="layout-2">
                  <div className="area-2-1 s3">
                  <div className="impressum-header">
                    {/* <button onClick={() => navigate(-1)}>Zurück</button> */}
                    <button onClick={() => navigate("/home")}>Home</button>
                    </div>
                    <h1 className="headline_1">Datenschutzerklärung</h1>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div className="layout-20">
          <div className="layout-20-inner mt-2 mb-4 use-parallax">
            <div className="main-inner">
              <div className="area-20-1 s4">
                <div className="template_box datenschutz_kk">
                  <div className="layout-2">
                    <div className="area-2-1 s3">
                      
                      <div class="area-2-1 s3">
                        <div class="wysiwyg_1   "><p><a href="#DS100"><strong>1. Absatz</strong></a></p>
                      </div>
                      <div>
                        <h2>1. Absatz</h2>
                        <p>
                          Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
                        </p>
                        <p>
                          Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
                        </p>
                      </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        {/* Weitere Abschnitte */}
      </div>
    </div>
  );
};

export default DataPrivacy;