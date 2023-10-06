import { FrappeProvider, useFrappeGetDocList } from "frappe-react-sdk";

const Home = () => {
    const {data, isLoading,error} = useFrappeGetDocList('Serial No')
    console.log('data:', data, isLoading, error)
    return (
        <>
        <FrappeProvider>
        <div>Hello React</div>
        </FrappeProvider>
       
        </>
    )
}
export default Home;