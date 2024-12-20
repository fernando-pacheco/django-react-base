import { ButtonCard } from "@/components/molecules/button-card"
import { BaseProps } from "@/interface/interface-base"
import { BaseService } from "@/service/base"
import { useEffect, useState } from "react"
import { useNavigate } from "react-router-dom"

export function Home() {
    const navigate = useNavigate()
    const [data, setData] = useState<BaseProps[]>([
        {
            id: 1,
            name: "",
            base_uuid: "",
        },
    ])

    useEffect(() => {
        async function fetchData() {
            const service = new BaseService()
            const response = await service.get()

            if (response) {
                setData(response)
            }
        }

        fetchData()
    }, [])

    return (
        <div className="flex flex-col flex-1 w-full h-screen justify-center items-center gap-10">
            <ButtonCard
                action={() => navigate("/")}
                text="Redirecionar para tela inicial"
            />

            <div className="flex gap-10">
                {data.map((item) => (
                    <div className="flex flex-col justify-center items-center gap-2">
                        <span className="text-white">{item.id}</span>
                        <span className="text-white">{item.name}</span>
                        <span className="text-white">{item.base_uuid}</span>
                    </div>
                ))}
            </div>
        </div>
    )
}
