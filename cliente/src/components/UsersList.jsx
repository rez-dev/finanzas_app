import { useEffect, useState } from "react";
import { getAllUsers } from "../api/users.api";
import { UserCard } from "./UserCard";

export function UsersList() {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    async function loadUsers() {
      const respuesta = await getAllUsers();
      setUsers(respuesta.data);
    }
    loadUsers();
  }, []);

  return (
    <div>
      {users.map((user) => (
        <UserCard key={user.id} user={user} />
      ))}
    </div>
  );
}
