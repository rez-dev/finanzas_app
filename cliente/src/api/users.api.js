import axios from 'axios'

const userApi = axios.create({
    baseURL: 'http://localhost:8000/transactions/api/v1/users/'
})

export const getAllUsers = () => {
    return userApi.get('/')
}

export const createUser = (user) => {
    return userApi.post('/', user)
}