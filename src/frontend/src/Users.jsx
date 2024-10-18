import React, { useEffect, useState } from "react";

const Users = () => {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch("http://127.0.0.1:5000/api/users");
        if (!response.ok) {
          throw new Error("Network response was not ok");
        }
        const result = await response.json();
        setData(result);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error: {error}</p>;

  return (
    <div className="card mt-2">
      <div className="card-body">
        {data.map((user) => (
          <div id={"user-id-" + user.id} key={user.id}>
            <h4>id = {user.id}</h4>
            <p>{user.name}</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Users;
