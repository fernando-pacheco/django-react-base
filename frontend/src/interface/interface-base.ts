export interface InterfaceBaseProps {
    id: string
    value: number
    contracts: ContractProps[]
    current: boolean
    participants: string[]
}

export interface ContractProps {
    id: number
    clause: string
}

export interface BaseProps {
    id: number
    name: string
    base_uuid: string
}
