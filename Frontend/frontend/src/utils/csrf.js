  // Read cookies 
  export function getCookie(name) {
    const cookieString = document.cookie;
    const cookies = cookieString.split('; ');
    for (const cookie of cookies) {
        const [key, value] = cookie.split('=');
        if (key === name) {
            return decodeURIComponent(value);
        }
    }
    return null; // Cookie was not found
}

  // Ask for CSRF-Cookie and token from django
  export async function getCsrfToken() {
      const response = await fetch(`http://127.0.0.1:8000/api/csrf-token/`, {
        credentials: 'include',
      });
    const data = await response.json();
    var csrfToken = getCookie('csrftoken'); // Get the cookie from django
    document.cookie = "csrfToken="+csrfToken; // Set the cookie in the browser
    return data.csrftoken; //Retunr the CSRF-Token
  };