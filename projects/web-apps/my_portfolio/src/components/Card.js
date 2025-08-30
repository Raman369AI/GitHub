import React from "react";
import {
  Heading,
  HStack,
  Image,
  Text,
  VStack,
  Box,
  Link,
  Button,
  useDisclosure,
  Modal,
  ModalOverlay,
  ModalContent,
  ModalHeader,
  ModalCloseButton,
  ModalBody,
  ListItem,
  OrderedList,
  AspectRatio
} from "@chakra-ui/react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faCode } from "@fortawesome/free-solid-svg-icons";
import { motion } from "framer-motion";

const AnimatedBox = motion(Box);

const Card = ({ title, description, imageSrc, url }) => {
  const { isOpen, onOpen, onClose } = useDisclosure();

  return (
    <AnimatedBox
      p={4}
      bg="#edb1f1"
      color="black"
      borderRadius="xl"
      whileHover={{ scale: 1.05, boxShadow: "0px 4px 8px rgba(0, 0, 0, 0.2)" }}
      transition={{ duration: 0.3 }}
      style={{ height: "100%", display: "flex", flexDirection: "column" }}
    >
      <VStack
        spacing={4}
        h="100%"
        justifyContent="space-between"
        flexGrow={1}
      >
        <AspectRatio ratio={16 / 9} w="100%">
          <Image
            src={imageSrc}
            alt={title}
            borderRadius="xl"
            objectFit="cover"
          />
        </AspectRatio>
        <VStack alignItems="flex-start" spacing={2} w="100%">
          <Heading as="h3" size="md">
            {title}
          </Heading>
          <Text color="#64748b" noOfLines={3}>
            {description[0]}
            {description.length > 1 && "..."}
          </Text>
          <HStack spacing={4} mt="auto">
            {url && (
              <Link href={url} isExternal>
                <Button
                  leftIcon={<FontAwesomeIcon icon={faCode} />}
                  colorScheme="purple"
                  size="sm"
                >
                  GitHub
                </Button>
              </Link>
            )}
            <Button colorScheme="purple" size="sm" onClick={onOpen}>
              Read More
            </Button>
          </HStack>
        </VStack>
      </VStack>

      {/* Modal for Full Description */}
      <Modal isOpen={isOpen} onClose={onClose} size="xl">
        <ModalOverlay />
        <ModalContent>
          <ModalHeader>{title}</ModalHeader>
          <ModalCloseButton />
          <ModalBody>
            <OrderedList pl={5} spacing={1}>
              {description.map((item, idx) => (
                <ListItem key={idx}>{item}</ListItem>
              ))}
            </OrderedList>
          </ModalBody>
        </ModalContent>
      </Modal>
    </AnimatedBox>
  );
};

export default Card;
